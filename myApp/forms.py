from django.contrib.auth.models import User
from django import forms
from .models import Post, Offer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'Degree_Program_or_Office', 'password']
        
class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['item_name', 'image', 'tags', 'quantity', 'condition']
        
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['item', 'bid']
        
    def __init__(self, username=None, *args, **kwargs):
        user = kwargs.pop('user')
        super(OfferForm, self).__init__(*args, **kwargs)
        if username is not None:
            try:
                username = User.objects.get(id=user)

                try:
                    items = Item.objects.filter(userName=username)
                    self.fields['item'] = forms.ModelChoiceField(queryset=items, widget=forms.Select(attrs={'required': False}), label='Item Offer', required=False)
                    self.fields['item'].label_from_instance = lambda obj: "%s" % obj.name
                except Item.DoesNotExist:
                    pass
            except User.DoesNotExist:
                pass