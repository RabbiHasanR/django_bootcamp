from django import forms
from django.core import validators
from user_profile.models import User
#
# def check_for_name(value):
#     if value[0].isdigit():
#         raise forms.ValidationError('Name needs to start with alphabet!')
class FormName(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
    # name=forms.CharField(validators=[check_for_name])
    # email=forms.EmailField()
    # varify_email=forms.EmailField(label='Enter your email again:')
    # text=forms.CharField(widget=forms.Textarea)
    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    # def clean(self):
    #     all_clean_data=super().clean()
    #     email=all_clean_data['email']
    #     vemail=all_clean_data['varify_email']
    #
    #     if email!=vemail:
    #         raise forms.ValidationError('Make sure email match!')
