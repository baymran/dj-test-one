from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Заголовок новости'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                 'placeholder': 'Введите текст новости',
                 'style': 'resize: none',
                 'rows': '5'}),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=100,
#                             min_length=4,
#                             label='Наименование',
#                             widget=forms.TextInput(attrs=
#                                                    {'class': 'form-control form-control-lg',
#                                                     'placeholder': 'Заголовок новости'})
#                             )
#     content = forms.CharField(label='Текст',
#                               required=False,
#                               widget=forms.Textarea(attrs=
#                                                     {'class': 'form-control',
#                                                      'placeholder': 'Введите текст новости',
#                                                      'style': 'resize: none',
#                                                      'rows': '5'})
#                               )
#     is_published = forms.BooleanField(label='Опубликовано',
#                                       initial=True,
#                                       widget=forms.CheckboxInput(attrs=
#                                                                  {'class': 'form-check-input',
#                                                                   'type': 'checkbox'})
#                                       )
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория',
#                                       empty_label=None,
#                                       widget=forms.Select(attrs=
#                                                                  {'class': 'form-select',
#                                                                   })
#                                       )
