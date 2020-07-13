from django import forms
from django.core import validators

class fillSlambook(forms.Form):
    # Your Questions Goes inside labels
    ghissu_meter = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10', 'class':"slider", 'id':"myRange"}), required=False, label="Ghissu Meter")
    phodu_meter = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10', 'class':"slider2", 'id':"myRange2"}), required=False, label="Phodu Meter")
    ans1 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 1 goes here", required=False)
    ans2 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 2 goes here", required=False)
    ans3 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 3 goes here", required=False)
    ans4 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 4 goes here", required=False)
    ans5 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 5 goes here", required=False)
    ans6 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 6 goes here", required=False)
    ans7 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 7 goes here", required=False)
    ans8 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 8 goes here", required=False)
    ans9 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 9 goes here", required=False)
    ans10 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 10 goes here", required=False)
    ans11 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 11 goes here", required=False)
    ans12 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 12 goes here", required=False)
    ans13 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 13 goes here", required=False)
    ans14 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 14 goes here", required=False)
    ans15 = forms.CharField(widget=forms.Textarea(attrs={}), label="question 15 goes here", required=False)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])