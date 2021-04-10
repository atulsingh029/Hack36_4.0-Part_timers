from django import forms


class SignInForm(forms.Form):
    email = forms.CharField(max_length=255, required=True, label='Email', widget=forms.EmailInput)
    password = forms.CharField(max_length=512, label='Password', required=True, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=255, min_length=3, required=True, label='First Name')
    last_name = forms.CharField(max_length=255, min_length=3, required=True, label='last Name')
    email = forms.EmailField(max_length=155, required=True, label='Email')
    password1 = forms.CharField(max_length=512,widget=forms.PasswordInput, label='Password', required=True)
    password2 = forms.CharField(max_length=512, widget=forms.PasswordInput, label='Confirm Password', required=True)
    you_are = forms.ChoiceField(choices=(('volunteer', 'volunteer'), ('victim', 'victim')))
    profession = forms.CharField(max_length=255)
    profile_pic = forms.ImageField(label='Profile Picture', allow_empty_file=True, required=False)


class HelpForm(forms.Form):
    help_message = forms.CharField(max_length=1024, label='Help Message', )
    contact_details = forms.CharField(max_length=1024, label='Conatct Details', )
