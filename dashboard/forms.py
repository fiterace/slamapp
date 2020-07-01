from django import forms
from django.core import validators

class fillSlambook(forms.Form):
    # Your Questions Goes inside labels
    ans1 = forms.CharField(widget=forms.Textarea,label="questions goes here")
    ans2 = forms.CharField(widget=forms.Textarea)
    ans3 = forms.CharField(widget=forms.Textarea)
    ans4 = forms.CharField(widget=forms.Textarea)
    ans5 = forms.CharField(widget=forms.Textarea)
    ans6 = forms.CharField(widget=forms.Textarea)
    ans7 = forms.CharField(widget=forms.Textarea)
    ans8 = forms.CharField(widget=forms.Textarea)
    ans9 = forms.CharField(widget=forms.Textarea)
    ans10 = forms.CharField(widget=forms.Textarea)
    ans11 = forms.CharField(widget=forms.Textarea)
    ans12 = forms.CharField(widget=forms.Textarea)
    ans13 = forms.CharField(widget=forms.Textarea)
    ans14 = forms.CharField(widget=forms.Textarea)
    ans15 = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])