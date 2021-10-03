from django import forms

class RegisterContact(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    Subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))