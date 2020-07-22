from django import forms
from django.core import validators

class fillSlambook(forms.Form):
    # Your Questions Goes inside labels
    ghissu_meter = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10', 'class':"slider", 'id':"myRange", 'value':'5'}), required=False, label="Ghissu Meter")
    phodu_meter = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '0', 'max': '10', 'class':"slider2", 'id':"myRange2", 'value':'5'}), required=False, label="Phodu Meter")
    ans1 = forms.CharField(widget=forms.Textarea(attrs={}), label="Your creative name (you can leave a hint for him/her or write anonymously or simply write your name)", required=True)
    ans2 = forms.CharField(widget=forms.Textarea(attrs={}), label="First impression?", required=True)
    ans3 = forms.CharField(widget=forms.Textarea(attrs={}), label="Best/First moment you shared with him/her:", required=False)
    ans4 = forms.CharField(widget=forms.Textarea(attrs={}), label="Pick one thing you wanna steal from him/her:", required=False)
    ans5 = forms.CharField(widget=forms.Textarea(attrs={}), label="Any fantasy you have related to him /her:", required=False)
    ans6 = forms.CharField(widget=forms.Textarea(attrs={}), label="What do you like about him/her:", required=False)
    ans7 = forms.CharField(widget=forms.Textarea(attrs={}), label="If you were to write his/her biography, what would you name it? ✍🏻", required=False)
    ans8 = forms.CharField(widget=forms.Textarea(attrs={}), label="Which fictional character is resembled the best by him/her?", required=False)
    ans9 = forms.CharField(widget=forms.Textarea(attrs={}), label="If you were to dedicate a place or building in campus to him/her, what funny name would you give it? 🏛️", required=False)
    ans10 = forms.CharField(widget=forms.Textarea(attrs={}), label="One thing that you know about him/her (he/she has no idea about that you know it since a long time) :", required=False)
    ans11 = forms.CharField(widget=forms.Textarea(attrs={}), label="One embarrassing moment that you have faced with her /him 😅:", required=False)
    ans12 = forms.CharField(widget=forms.Textarea(attrs={}), label="With whom would you want to pair him/her (sasta/sasti love guru to ho hi tum, chalo batao 😜):", required=False)
    ans13 = forms.CharField(widget=forms.Textarea(attrs={}), label="She/He has a love/hate relationship with _ (a debater friend/ex/ profs😛):", required=False)
    ans14 = forms.CharField(widget=forms.Textarea(attrs={}), label="One 'BAKCHODI BHARA KAAM' you always wanted to learn from him/her but didn't get that golden chance:", required=False)
    ans15 = forms.CharField(widget=forms.Textarea(attrs={}), label="If not engineering, what profession would this person be in?", required=False)
    ans16 = forms.CharField(widget=forms.Textarea(attrs={}), label="Your heartfelt final message before they leave:", required=False)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])