from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # внешний вид формы
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    def clean_title(self): # автоматическая валидация title
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title

    class Meta:
        model = Advertisement  # имя модели
        fields = ("title", "description", "image", "price", "auction")  # поля в форме (названия из модели)








# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
#

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64)
#     description = forms.CharField()
#     price = forms.DecimalField()
#     auction = forms.BooleanField(required=False)
#     image = forms.ImageField()