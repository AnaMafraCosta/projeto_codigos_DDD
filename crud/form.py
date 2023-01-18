from .models import DDD
from django.forms import ModelForm

class DDDForm(ModelForm):
    class Meta:
        model = DDD
        fields = ["ddd", "cidade", "estado"]