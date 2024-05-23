import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _

@deconstructible
class CustomASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        '아이디는 영어 대소문자, 숫자, 밑줄(_)만 포함해야 합니다.'
    )


@deconstructible
class CustomASCIIPasswordValidator(validators.RegexValidator):
    regex = r'^(?=.*[\d])(?=.*[a-zA-Z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{6,}$'
    message = _(
        '비밀번호는 6자 이상의 영문과 숫자, 특수문자를 포함하여야 합니다.'
    )