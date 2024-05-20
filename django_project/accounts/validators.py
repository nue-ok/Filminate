import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _

@deconstructible
class CustomASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        '이상한 특수문자 사용하지 마세요.'
    )