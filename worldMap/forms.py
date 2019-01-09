from django import forms
from .models import Attack


class AttackForm(forms.ModelForm):
    class Meta:
        model = Attack
        fields = ['attacker', 'defender', 'arrive', 'send']
