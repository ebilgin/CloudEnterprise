import re
from django import forms,template
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    company_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    
    domain_name = forms.RegexField(regex=r'^\w+$', max_length=30, error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    user_name = forms.RegexField(regex=r'^\w+$', max_length=30, error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=30)))
    password_conf = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=30)))
    
    agree_terms = forms.BooleanField(widget=forms.CheckboxInput())
    
   
 #    
 #    
 #    
 #    
 #    
 #    def clean_username(self):
 #        try:
 #            user = User.objects.get(username__iexact=self.cleaned_data['username'])
 #        except User.DoesNotExist:
 #            return self.cleaned_data['username']
 #        raise forms.ValidationError(_("The username already exists. Please try another one."))
 # 
 #    def clean(self):
 #        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
 #            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 #                raise forms.ValidationError(_("The two password fields did not match."))
 #        return self.cleaned_data
 #==============================================================================
    
    
 