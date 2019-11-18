from django import forms
from django.core.validators import RegexValidator
from re import IGNORECASE


class RepoForm(forms.Form):
    author = forms.CharField(
        min_length=3,
        max_length=39,
        validators=[
            RegexValidator(
                r'^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$',
                message="Author should be a combination of Alphabets and Numbers",
                code='invalid_author', flags=IGNORECASE),
        ]
    )
