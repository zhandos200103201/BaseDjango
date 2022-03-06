from .models import Celebrities, Film, Literature, Maths
from django.forms import ModelForm, TextInput, Textarea


class CelebrityForm(ModelForm):
    class Meta:
        model = Celebrities
        fields = ["title", "description", "link", "type"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите биографию'
            }),
            "link": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
        }



class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["title", "description", "link", "type"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите биографию'
            }),
            "link": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
        }


class LiteratureForm(ModelForm):
    class Meta:
        model = Literature
        fields = ["title", "description", "link", "type"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите биографию'
            }),
            "link": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
        }


class MathsForm(ModelForm):
    class Meta:
        model = Maths
        fields = ["title", "description", "link", "type"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите биографию'
            }),
            "link": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
        }