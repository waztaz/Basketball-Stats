from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from roster.models import (Player, Coach, User)

class PlayerSignUpForm(UserCreationForm):
    name=forms.CharField(label='Your name', max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        player = Player.objects.create(user=user, name=self.data['name'])
        return user
'''
class CoachSignUpForm(UserCreationForm):
    name=forms.CharField(label='Your name', max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user, name=self.data['name'])
'''
