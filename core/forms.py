from django import forms                              

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
        error_messages={
            'required': 'Name is required.',
            'min_length': 'Name must be at least 3 characters long'
        }
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )
    subject = forms.CharField(
        max_length=20,
        min_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
        error_messages={
            'required': 'Subject is required.',
            'min_length': 'Subject must be atleast 5 characters',
            'max_length': 'Subject must be maximum 20 charcters'
        }
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your message here...'}),
        error_messages={
            'required': 'Message is required',
            'min_length': 'Message must be atleast 20 characters'
        }
    )
