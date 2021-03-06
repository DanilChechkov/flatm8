import datetime
from typing import MutableMapping
from django.contrib.auth.models import User

from .models import Profile,Chatroom

def searchmatches():
    #Friend.objects.all().delete()
    profileList = Profile.objects.values()
    
    now = datetime.datetime.now()
    checked = []
    for me in profileList:
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
        #print(myAge,myRAge,myPrice,myRTime,mySubway,myHrono,myCOMU,myBadic,myOrgL,
        #myTemp,mySouL,myClean,myGuest,mymoL,myGen,myRGen,myRel,myRRel,myFrtime,myPets, sep='\n')
        
        for you in profileList:
            if me == you or [me.get('user_id'),you.get('user_id')] in checked: continue
            #print('AND')
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
            #print(hAge,hRAge,hPrice,hRTime,hSubway,hHrono,hCOMU,hBadic,hOrgL,
            #hTemp,hSouL,hClean,hGuest,hmoL,hGen,hRGen,hRel,hRRel,hFrtime,hPets, sep='\n')

            #MAIN FILTERS: AGE,PRICE,RELIGY,GENDER,
            if not hRAge[0]<=myAge<=hRAge[1] or not myRAge[0]<=hAge<=myRAge[1]: continue
            if not (hPrice[0]<=myPrice[1]<=hPrice[1] or myPrice[0]<=hPrice[1]<=myPrice[1]):continue
            if not ((hRRel == myRel or hRRel == 'nosing') and (myRRel == hRel or myRRel == 'nosing')): continue
            if not ((hRGen == myGen or hRGen == 'inbetween') and (myRGen == hGen or myRGen == 'inbetween')): continue

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
            capa = 100*points/16

            mUser = User.objects.get(id=me.get('user_id'))
            hUser = User.objects.get(id=you.get('user_id'))
            chatlist = Chatroom.objects.values()
            if checkChatr(mUser,hUser,chatlist,capa,subinte):
                createChatroom(mUser,hUser,capa,subinte)

    checked = []

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