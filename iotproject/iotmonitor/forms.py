from django import forms

from .models import Reading

class Leitura(forms.ModelForm):

    class Meta:
        model = Reading
        fields = ('sensor_name', 'value')


#Criaremos um link para a página, uma URL, uma view e um template.