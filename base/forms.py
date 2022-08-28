from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # take all attributes from Room (later only list of specific attributes)
        fields = '__all__'
        exclude = ['host', 'participants']
