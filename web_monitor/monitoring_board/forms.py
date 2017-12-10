from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(max_length=200)
    name = forms.CharField(max_length=500)
    urls = forms.CharField()
    dates = forms.CharField()


class PageForm(forms.Form):
    contact_id = forms.IntegerField()
    url = forms.CharField(max_length=200)
    date = forms.DateTimeField()