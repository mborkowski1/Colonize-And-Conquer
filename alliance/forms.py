from django import forms
from .models import Alliance
from raports.models import AllianceInvite


class CreateAllianceForm(forms.ModelForm):
    class Meta:
        model = Alliance
        fields = ['name', 'alliance_logo', 'alliance_bio']


class CreateAllianceInviteForm(forms.ModelForm):
    class Meta:
        model = AllianceInvite
        fields = ['receiver', 'name']
