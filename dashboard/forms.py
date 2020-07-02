from django import forms
from django.core import validators

class fillSlambook(forms.Form):
    # Your Questions Goes inside labels
    ans1 = forms.CharField(widget=forms.Textarea(attrs={}),label="questions goes here")
    ans2 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans3 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans4 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans5 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans6 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans7 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans8 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans9 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans10 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans11 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans12 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans13 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans14 = forms.CharField(widget=forms.Textarea(attrs={}))
    ans15 = forms.CharField(widget=forms.Textarea(attrs={}))
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])