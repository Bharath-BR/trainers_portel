from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):

    confirm_password=forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':"Re-Enter the password"
                }
            )
        )

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

        widgets={
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Enter the username'
                }
            ),

            'email':forms.EmailInput(
                attrs={
                    'placeholder':"Enter the email"
                }
            ),

            'password':forms.PasswordInput(
                attrs={
                    'placeholder':"Enter the password"
                }
            )
        }

    
    def clean_username(self):

        username=self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with username already exists!")

        return username

    def clean_email(self):
    
        email=self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with email already exists!")

        return email

    def clean_password(self):
        password=self.cleaned_data.get('password')

        if len(password)<8:
            raise forms.ValidationError("Password must contain atleast 8 characters")

        having_uc=False
        having_lc=False
        having_digit=False

        for char in password:
            if char.isupper():
                having_uc=True
            if char.islower():
                having_lc=True
            if char in "0123456789":
                having_digit=True
        if not having_lc or not having_uc or not having_digit:
            raise forms.ValidationError("Password must contain atleast one digit,one lower-case and one upper-case alphabet")
        return password

    # def create(self):
    #     username=self.cleaned_data.get('username')
    #     email=self.cleaned_data.get('email')
    #     password=self.cleaned_data.get('password')
    #     confirm_password=self.cleaned_data.get('confirm_password')

    #     if password==confirm_password:
    #         user=User.objects.create_user(username=username,email=email,password=password)
    #         return user
    #     else:
    #         self.add_error('confirm_password','Password and Confirm Password Missmatch!')
    


class UserLoginForm(forms.Form):

    username=forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'placeholder':'Enter the username'
                }
            )
        )

    password=forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':'Enter the password'
                }
            )
        )

   





    
