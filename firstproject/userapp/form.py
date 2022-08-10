import email
from django import forms
class userdata(forms.Form):
    name=forms.CharField(max_length=2,min_length=2,initial="",required=True)
    email=forms.EmailField(max_length=20,min_length=3,initial="",required=True)
    addr=forms.CharField(max_length=20,min_length=2,initial="",required=False)
    age=forms.IntegerField(max_value=200,min_value=18,initial="",required=True)
