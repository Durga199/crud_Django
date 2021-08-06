from django import forms
from sign.models import *


class sign1(forms.ModelForm):
    class Meta:
        model = account1
        fields = "__all__"

class sign2(forms.ModelForm):
    class Meta:
        model = Family
        fields = "__all__"