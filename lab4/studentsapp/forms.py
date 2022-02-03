from django import forms
from .models import *


class AddTrack(forms.ModelForm):
    class Meta:
        fields = '__all__'
        labels = {
            'track_name': 'Track Name'
        }
        model = Track


class InsertStudent(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['track_id'].widget.choices = [(track.track_id, track.track_name) for track in Track.objects.all()]

    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'std_id': 'ID',
            'std_fname': 'First Name',
            'std_lname': 'Last Name',
            'track_id': 'Track'
        }
