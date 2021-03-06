from re import VERBOSE
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import CheckboxInput, NumberInput, RadioSelect, TextInput, Textarea, Widget
from django_select2 import forms as s2forms
from .models import Profile,Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
        widgets = {
            'message':Textarea(attrs={'placeholder': 'Введите сообщение...'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name':TextInput(attrs={'placeholder': 'Имя'}),
            'last_name':TextInput(attrs={'placeholder': 'Фамилия'}),
            'email':TextInput(attrs={'placeholder': 'email@em.com'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','urAge','aprUGEN', 'abuCOMU','abuORGL','abrCLEAN','aprURRELIGY','abuBADIC','aprTELLUS',
                'abuLST','aprPETS','abrTEMP','aprFRETM',
                'rmAgeL','rmAgeU','aprR8GEN','aprR8RELIGY',
                'rntLPrice','rntUPrice','rntTime','rntCity','rntSubway','rntSubwayM','abrGUEST','abrSOUL','abrCOMMUNISM',
                'contInsta','contTeleg','contVKont','mesNotif','chatNotif')
        widgets = {
            'urAge':NumberInput(attrs={'min': '16','max':'99'}),
            'abuORGL':NumberInput(attrs={'min': '0','max':'10'}),
            'abrCLEAN':NumberInput(attrs={'min': '0','max':'30'}),
            'abrTEMP':NumberInput(attrs={'min': '12','max':'28'}),
            'abuBADIC':s2forms.Select2MultipleWidget({'data-language': 'ru','style':"width: 100%"}),
            'aprFRETM':s2forms.Select2MultipleWidget({'data-language': 'ru','style':"width: 100%"}),
            'rmAgeL':NumberInput(attrs={'min': '16','max':'99'}),
            'rmAgeU':NumberInput(attrs={'min': '16','max':'99'}),
            'rntSubway':s2forms.Select2MultipleWidget({'data-language': 'ru','style':"width: 100%"}),
            'rntSubwayM':s2forms.Select2MultipleWidget({'data-language': 'ru','style':"width: 100%"}),
            'rntUPrice':NumberInput(attrs={'min': '1000','max':'99999','step':'500'}),
            'rntLPrice':NumberInput(attrs={'min': '1000','max':'99999','step':'500'}),
            'rntTime':RadioSelect,
            'abuLST':RadioSelect,
            'abuCOMU':RadioSelect,
            'abrSOUL':RadioSelect,
            'abrGUEST':RadioSelect,
            'abrCOMMUNISM':RadioSelect,
            'aprPETS':RadioSelect,
            'contInsta':TextInput(attrs={'placeholder': 'Ваш ник в инстаграм без @'}),
            'contTeleg':TextInput(attrs={'placeholder': 'Укажите ваш ник в Telegram'}),
            'contVKont':TextInput(attrs={'placeholder': 'Укажите тут ваш id ВК'}),
            'mesNotif':CheckboxInput,
            'chatNotif':CheckboxInput,
        } 
        #exclude=['user']
        #rnSub = forms.MultipleChoiceField(choices=SUB_CHOICES, widget=forms.CheckboxSelectMultiple)

class LoginForm(forms.Form):
    username= forms.CharField(label="Логин")
    password= forms.CharField(widget=forms.PasswordInput,label='Пароль')

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={"maxlength":16}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
    