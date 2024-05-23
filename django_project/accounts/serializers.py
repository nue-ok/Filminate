# accounts/serializers.py
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from movies.serializers import *
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer

from rest_framework.validators import UniqueValidator
from .validators import CustomASCIIUsernameValidator, CustomASCIIPasswordValidator
from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model
UserModel = get_user_model()


# 프로필 페이지용
class UserSerializer(serializers.ModelSerializer):
    
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_movie_count = serializers.IntegerField(source='like_movie.count', read_only=True)
    
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'profile_image', 'review_count', 'comment_count', 'like_movie_count',)


# 회원정보 제공용
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)


# 회원가입용
class CustomRegisterSerializer(RegisterSerializer):
    # 필요한 필드들을 추가합니다.
    username = serializers.CharField(
        required=True,
        min_length=3,
        max_length=30,
        # multiple validators
        validators=[UniqueValidator(queryset=UserModel.objects.all(), message=('이미 존재하는 아이디입니다.')),
                    CustomASCIIUsernameValidator()],
    )
    password1 = serializers.CharField(
        write_only=True,
        validators=[CustomASCIIPasswordValidator()],
    )
    password2 = serializers.CharField(
        write_only=True,
    )
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("비밀번호가 일치하지 않습니다."))
        return data
    
    # profile_image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = UserModel
    
    # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),
        # 'profile_image': self.validated_data.get('profile_image', ''),
        }
    

# 로그인용
class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        user = self.get_auth_user(username, email, password)

        if not user:
            msg = _('아이디 또는 비밀번호가 틀렸습니다.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        # If required, is the email verified?
        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user, email=email)

        attrs['user'] = user
        return attrs


# 회원정보 수정용
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'profile_image',)
        # fields = ('username', 'email',)