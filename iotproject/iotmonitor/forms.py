from django import forms

from .models import Reading

class Leitura(forms.ModelForm):

    class Meta:
        model = Reading
        fields = ('name', 'sensor_read')


#Criaremos um link para a página, uma URL, uma view e um template.