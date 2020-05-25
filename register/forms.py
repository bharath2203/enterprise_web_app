from django import forms
from .models import Data


KANNADA_CATEGORY_CHOICES = [
    ('Text', 'ಪಠ್ಯ'), ('Audio', 'ಆಡಿಯೊ'), ('Image', 'ದ್ರುಶ್ಯ'), ('Video',
                                                                 'ದ್ರುಶ್ಯಾವಳಿ')
]

HINDI_CATEGORY_CHOICES = [
    ('Text', 'ಪಠ್ಯ'), ('Audio', 'ಆಡಿಯೊ'), ('Image', 'ದ್ರುಶ್ಯ'), ('Video',
                                                                 'ದ್ರುಶ್ಯಾವಳಿ')
]

CATEGORY_CHOICES = [
    ('Text', 'Text'), ('Audio', 'Audio'), ('Image', 'Image'), ('Video',
                                                               'Video')
]


class TextForm(forms.Form):
    text = forms.CharField(max_length=100)


class DataForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, widget=forms.RadioSelect)
    upload = forms.FileField()


class KannadaDataForm(forms.Form):

    text_id = forms.CharField(
        max_length=50, label='&#3253;&#3262;&#3221;&#3277;&#3247; <br/>')
    text = forms.CharField(widget=forms.Textarea,
                           label="&#3242;&#3232;&#3277;&#3247;")
    category = forms.ChoiceField(label='&#3253;&#3248;&#3277;&#3223;',
                                 choices=KANNADA_CATEGORY_CHOICES, widget=forms.RadioSelect)
    upload = forms.FileField(
        label="&#3205;&#3242;&#3277;&#3250;&#3275;&#3233;&#3277;")


class HindiDataForm(forms.Form):

    text_id = forms.CharField(
        max_length=50, label='&#3253;&#3262;&#3221;&#3277;&#3247; <br/>')
    text = forms.CharField(widget=forms.Textarea,
                           label="&#3242;&#3232;&#3277;&#3247;")
    category = forms.ChoiceField(label='&#3253;&#3248;&#3277;&#3223;',
                                 choices=HINDI_CATEGORY_CHOICES, widget=forms.RadioSelect)
    upload = forms.FileField(
        label="&#3205;&#3242;&#3277;&#3250;&#3275;&#3233;&#3277;")
