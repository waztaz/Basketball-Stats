from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from roster.models import (Player, Coach, User, Team)

class PlayerSignUpForm(UserCreationForm):
    POINT_GUARD = 'PG'
    SHOOTING_GUARD = 'SG'
    SMALL_FORWARD = 'SF'
    POWER_FORWARD = 'PF'
    CENTER = 'C'
    POSITION_CHOICES = (
        (POINT_GUARD, "Point Guard"),
        (SHOOTING_GUARD, "Shooting Guard"),
        (SMALL_FORWARD, "Small Forward"),
        (POWER_FORWARD, "Power Forward"),
        (CENTER, "Center"),
    )


    first_name=forms.CharField(label='First Name', max_length=50)
    last_name=forms.CharField(label='Last Name', max_length=50)
    height=forms.IntegerField(label='Height in inches')
    weight=forms.IntegerField(label='Weight in lbs')
    position=forms.ChoiceField(choices=POSITION_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        player = Player.objects.create(
                user=user,
                first_name=self.data['first_name'],
                last_name=self.data['last_name'],
                height=self.data['height'],
                weight=self.data['weight'],
                position=self.data['position']
                )
        return user

class CoachSignUpForm(UserCreationForm):
    first_name=forms.CharField(label='First Name', max_length=50)
    last_name=forms.CharField(label='Last Name', max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_coach = True
        user.save()
        coach = Coach.objects.create(user=user)

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'height', 'weight')
