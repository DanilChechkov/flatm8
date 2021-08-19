from django.contrib import admin
from .models import Profile,Message,Chatroom
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'first_name') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','active','urAge', 'rmAgeL','rmAgeU','aprUGEN','aprR8GEN','aprTELLUS','photo']
                #['user','active', 'urAge', 'rmAgeL','rmAgeU','rntLPrice','rntUPrice','rntTime','rntSubway',
                #'abuLST','abuCOMU','abuBADIC','abuORGL',
                #'abrTEMP','abrSOUL','abrCLEAN','abrGUEST','abrCOMMUNISM',
                #'aprUGEN','aprR8GEN','aprURRELIGY','aprR8RELIGY','aprFRETM','aprPETS','aprTELLUS','photo']
class MessageAdmin(admin.ModelAdmin):
    list_display = ['chat','author','message','is_readed']
class ChatAdmin(admin.ModelAdmin):
    list_display = ['get_members','cap','sub']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Chatroom,ChatAdmin)
# Register your models here.
