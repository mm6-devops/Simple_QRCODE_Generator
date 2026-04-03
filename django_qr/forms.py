from django import forms

class QRCODEFORM(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50, 
        label='Restaurant Name', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Restaurant Name'
            })
    )
    url = forms.URLField(
        max_length=200, 
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your URL Of Your Restaurant Name'
            })
        )