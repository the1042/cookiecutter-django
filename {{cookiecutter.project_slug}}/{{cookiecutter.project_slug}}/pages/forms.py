from django import forms

class ContactForm(forms.Form):
  from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}), required=True)
  subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), required=True)
  message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
  