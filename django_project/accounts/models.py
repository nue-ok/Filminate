from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review
from django.db import models
from allauth.account.adapter import DefaultAccountAdapter


def profile_image_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'


# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(default='default_image.jpg', upload_to=profile_image_path)
    nickname = models.CharField(max_length=100)
    like_movie = models.ManyToManyField(Movie, related_name='user_like_movie')
    like_review = models.ManyToManyField(Review, related_name='user_like_review')
    
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # nickname 필드를 추가
        nickname = data.get("nickname")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
