from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator, RegexValidator
from django import forms
from taxi.models import Driver


class DriverCreationForm(UserCreationForm):

    driver = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number",
            "first_name",
            "last_name",
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    LICENSE_LENGTH = 8
    LICENSE_PATTERN = r"^[A-Z]{3}\d{5}$"

    license_number = forms.CharField(
        max_length=LICENSE_LENGTH,
        required=True,
        validators=[
            MaxLengthValidator(LICENSE_LENGTH),
            RegexValidator(
                regex=LICENSE_PATTERN,
                message="License number must consist"
                        " of 3 uppercase letters followed"
                        " by 5 digits (e.g. ABC12345)"
            )
        ]
    )

    class Meta:
        model = Driver
        fields = ("license_number",)
