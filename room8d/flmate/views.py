from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

import datetime, os,pickle
from django.utils import timezone
from datetime import timedelta as td
from .models import Profile,Chatroom
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm,MessageForm,LoginForm
from room8d import settings
from django.core.mail import send_mail

def index(request):
    return render(request, 'account/index.html',{'section':'index'})
def google(request):
    return render(request, 'account/google3a35c7ffe9c8fa8e.html',{'section':'google'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user,'section':'reg'})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form,'section':'wrongreg'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    chats = Chatroom.objects.filter(members__in=[request.user.id])
                    return render(request, 'account/dialogs.html', {'user_profile': request.user, 'chats': chats,'section':'dialogs'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'account/login.html', {'form': form,
                                                'section':'invlogin'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form,
                                                'section':'login'})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            chats = Chatroom.objects.filter(members__in=[request.user.id])
            profileList = Profile.objects.values()
            request.user.profile.active = True
            request.user.profile.save()

            
            now = datetime.datetime.now()
            checked = []
            me = request.user.profile.__class__.objects.filter(pk=request.user.profile.id).values().first()
            myAge = int(me.get('urAge'))
            myRAge = [int(me.get('rmAgeL')),int(me.get('rmAgeU'))]
            myPrice = [int(me.get('rntLPrice')),int(me.get('rntUPrice'))]
            myRTime = str(me.get('rntTime'))
            mySubway = [ x for x in me.get('rntSubway')]
            myHrono = str(me.get('abuLST'))
            myCOMU = str(me.get('abuCOMU'))
            myBadic = [ x for x in me.get('abuBADIC')]
            myOrgL = int(me.get('abuORGL'))
            myTemp = int(me.get('abrTEMP'))
            mySouL = str(me.get('abrSOUL'))
            myClean = int(me.get('abrCLEAN'))
            myGuest = str(me.get('abrGUEST'))
            mymoL = str(me.get('abrCOMMUNISM'))
            myGen = str(me.get('aprUGEN'))
            myRGen = str(me.get('aprR8GEN'))
            myRel = str(me.get('aprURRELIGY'))
            myRRel = str(me.get('aprR8RELIGY'))
            myFrtime = [ x for x in me.get('aprFRETM')]
            myPets = str(me.get('aprPETS'))
            
            for you in profileList:
                if not you.get('active'):
                    inactiveUser = User.objects.get(id=you.get('user_id'))
                    lastlog = inactiveUser.last_login
                    lastpos = timezone.now() - td(days=21)
                    if(inactiveUser.profile.aprTELLUS == 'Мне было лень это менять.'):
                        inactiveUser.profile.aprTELLUS = 'Мне было лень это менять!'
                        inactiveUser.profile.active = False
                        inactiveUser.profile.save()
                        inactiveUser.email_user("FLATMATE - остался всего один шаг!", 
                                'Привет! Ты создал аккаунт, но не заполнил профиль на сайте=( Мы сможем подобрать тебе подходящего соседа, только когда ты закончишь этот шаг. Заходи на сайт во вкладку ПРОФИЛЬ! --> https://flatm8.ru/', 
                                    'flatmate@flatm8.ru')
                    if lastlog<lastpos:
                        for chat in Chatroom.objects.all():
                            if inactiveUser in chat.members.all():
                                chat.delete()
                        inactiveUser.profile.delete()
                        inactiveUser.delete()
                    continue
                else:
                    UserToSwitch = User.objects.get(id=you.get('user_id'))
                    lastlog = UserToSwitch.last_login
                    lastpos = timezone.now() - td(days=14)
                    if lastlog<lastpos:
                        #DEACTIVE PROFILE CUZ USER HAVEN'T VISIT SITE FOR 14 DAYS
                        UserToSwitch.profile.active = False
                        UserToSwitch.profile.save()
                        UserToSwitch.email_user("FLATMATE - твой аккаунт деактивирован!", 
                                'Привет! Сайт растет и число пользователей ежедневно увеличивается! Ты не заходил на сайт более двух недель и мы решили, что ты больше не ищешь соседа, поэтому деактивировали твой профиль. Если мы ошиблись - заходи на сайт, открой вкладку "ПРОФИЛЬ" и нажми сохранить изменения, иначе твой аккаунт будет безвозвратно удален через неделю! --> https://flatm8.ru/', 
                                    'flatmate@flatm8.ru')
                        
                if me == you or [me.get('user_id'),you.get('user_id')] in checked: continue
                points = 0
                frtme = 0
                subinte=0

                hAge = int(you.get('urAge'))
                hRAge = [int(you.get('rmAgeL')),int(you.get('rmAgeU'))]
                hPrice = [int(you.get('rntLPrice')),int(you.get('rntUPrice'))]
                hRTime = str(you.get('rntTime'))
                hSubway = [ x for x in you.get('rntSubway')]
                hHrono = str(you.get('abuLST'))
                hCOMU = str(you.get('abuCOMU'))
                hBadic = [ x for x in you.get('abuBADIC')]
                hOrgL = int(you.get('abuORGL'))
                hTemp = int(you.get('abrTEMP'))
                hSouL = str(you.get('abrSOUL'))
                hClean = int(you.get('abrCLEAN'))
                hGuest = str(you.get('abrGUEST'))
                hmoL = str(you.get('abrCOMMUNISM'))
                hGen = str(you.get('aprUGEN'))
                hRGen = str(you.get('aprR8GEN'))
                hRel = str(you.get('aprURRELIGY'))
                hRRel = str(you.get('aprR8RELIGY'))
                hFrtime = [ x for x in you.get('aprFRETM')]
                hPets = str(you.get('aprPETS'))

                checked.append([me.get('user_id'),you.get('user_id')])
                checked.append([you.get('user_id'),me.get('user_id')])

                #MAIN FILTERS: AGE,PRICE,RELIGY,GENDER,
                if not hRAge[0]<=myAge<=hRAge[1] or not myRAge[0]<=hAge<=myRAge[1]: continue
                if not (hPrice[0]<=myPrice[1]<=hPrice[1] or myPrice[0]<=hPrice[1]<=myPrice[1]):continue
                if not ((hRRel == myRel or hRRel == 'nosing') and (myRRel == hRel or myRRel == 'nosing')): continue
                if not ((hRGen == myGen or hRGen == 'inbetween') and (myRGen == hGen or myRGen == 'inbetween')): continue
                if myRTime != hRTime: continue
                points += 15

                #COUNT POINTS, NOT VERY IMPORTANT POINTS
                if myRTime == hRTime: points +=1                #TERM
                if myHrono == hHrono: points +=1                 #Hronos
                if myCOMU == hCOMU: points +=1                   #Extrav/Introv
                if myOrgL-2<=hOrgL<=myOrgL+2: points +=1        #Organisation level
                if myTemp-2<=hTemp<=myTemp+2: points +=1        #Comfort temperature
                if mySouL == hSouL:points +=1                   #Sound level
                if myClean-2<=hClean<=myClean+2: points +=1     #Cleaning
                if myGuest == hGuest:points +=1                 #Guests
                if mymoL == hmoL:points +=1                     #COMMUNISM  
                if myPets==hPets or (myPets == 'nomater' or hPets == 'nomater'): points +=1  #PETS
                if len(list(set(myFrtime)&set(hFrtime))) != 0:
                    points += int((len(list(set(myFrtime)&set(hFrtime)))/10)*5) #Freetime intersections MAX 5POINTS!!!

                #SPECIAL SUBWAY FIELD, EVEN IF NO MATCH IT STILL COUNTS, BUT LATER subinte WILL SAY NO/YES MATCHES SUBWAY
                subInter = list(set(mySubway)&set(hSubway))
                if len(subInter)==0: subinte = 1

                #Bad addictions
                badInter = list(set(myBadic)&set(hBadic))
                if len(badInter)>0: points +=1
                #SAVING ROOMATES
                capa = 100*points/31

                
                mUser = User.objects.get(id=me.get('user_id'))
                hUser = User.objects.get(id=you.get('user_id'))
                chatlist = Chatroom.objects.values()
                print(mUser.email)
                if checkChatr(mUser,hUser,chatlist,capa,subinte):
                    createChatroom(mUser,hUser,capa,subinte)
                    #NOTIFICATION SYSTEM
                    notifFILE = settings.BASE_DIR +'/notification.pkl'
                    notiData = {}
                    if hUser.profile.chatNotif:
                        if os.path.exists(notifFILE):
                            with open(notifFILE, 'rb') as f:
                                notiData = pickle.load(f)
                        if not hUser.email in notiData.keys():
                            notiData[hUser.email] = [timezone.now().date() -td(days=1),timezone.now().date() -td(days=1)]
                        if timezone.now().date() > notiData[hUser.email][0]:
                            hUser.email_user("FLATMATE - мы нашли тебе соседа!", 
                                    'Привет! Мы нашли тебе соседа, осталось только написать ему! --> https://flatm8.ru/dialogs/\nКстати от уведомлений можно отписаться тут --> https://flatm8.ru/edit/\nЕсли что-то работает не так дай нам об этом знать - DanilChechkov@flatm8.ru', 
                                        'flatmate@flatm8.ru')
                            #txt = 'succes'
                            #send_mail("TEST",txt,'flatmate@flatm8.ru',['danilchechkov@icloud.com'])
                            notiData[hUser.email][0] = timezone.now().date()+td(days=3)
                        with open(notifFILE, 'wb') as f:
                            pickle.dump(notiData, f)
                    #NOTIF SYS OVER

            checked = []
            return render(request, 'account/dialogs.html', {'user_profile': request.user, 'chats': chats,'section':'dialogs'})
        else:
            print('fuck')
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
            img = request.user.profile.photo
            if not img: img=''
            return render(request,
                        'account/edit.html',
                        {'user_form': user_form,
                        'profile_form': profile_form,'section':'edit','img':img})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        img = request.user.profile.photo
        if not img: img=''
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,'section':'edit','img':img})

def checkChatr(mUser,hUser,cht,cap,sub):
    for idm in cht:
        chatf = Chatroom.objects.get(id=idm.get('id'))
        if mUser in chatf.members.all() and hUser in chatf.members.all():
            if chatf.cap != cap or chatf.sub !=sub:
                chatf.cap = cap 
                chatf.sub = sub
                chatf.save()
            return 0
    return 1

def createChatroom(mUser,hUser,cap,sub):
    ourchat=Chatroom.objects.create(cap=cap,sub=sub)
    ourchat.save()
    ourchat.members.add(mUser)
    ourchat.save()
    ourchat.members.add(hUser)
    ourchat.save()

@login_required
def dialog(request):
    dat = {}
    with open(settings.BASE_DIR +'/notification.pkl', 'rb') as f:
        dat =pickle.load(f)
    for email in dat:
        if timezone.now().date() > dat[email][0]:
            print(email,dat[email],sep='\t')
    chats = Chatroom.objects.filter(members__in=[request.user.id])
    return render(request, 'account/dialogs.html', {'user_profile': request.user, 'chats': chats,'section':'dialogs'})

@login_required
def messages(request,chat_id):
    if request.method == 'GET':
        try:
            chat = Chatroom.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chatroom.DoesNotExist:
            chat = None
        return render(
            request,
            'account/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )
    else:
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()

            #NOTIFICATION SYSTEM
            notifFILE = settings.BASE_DIR +'/notification.pkl'
            notiData = {}
            chat = Chatroom.objects.get(id=chat_id)
            cmembers = chat.members.all()
            hUser = cmembers[0] if cmembers[0]!=request.user else cmembers[1]
            if hUser.profile.mesNotif:
                if os.path.exists(notifFILE):
                    with open(notifFILE, 'rb') as f:
                        notiData = pickle.load(f)
                if not hUser.email in notiData.keys():
                    notiData[hUser.email] = [timezone.now().date() -td(days=1),timezone.now().date() -td(days=1)]
                if timezone.now().date()>notiData[hUser.email][1]:
                    hUser.email_user("FLATMATE - у тебя новое сообщение!", 
                            'Привет! Твой идеальный сосед уже написал тебе! --> https://flatm8.ru/dialogs/\nКстати от уведомлений можно отписаться тут --> https://flatm8.ru/edit/\nЕсли что-то работает не так - дай нам об этом знать - DanilChechkov@flatm8.ru', 
                                'flatmate@flatm8.ru')
                    notiData[hUser.email][1] = timezone.now().date()+td(days=3)
                with open(notifFILE, 'wb') as f:
                    pickle.dump(notiData, f)
            #NOTIF SYS OVER
        try:
            chat = Chatroom.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chatroom.DoesNotExist:
            chat = None
        return render(
            request,
            'account/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            })
    
