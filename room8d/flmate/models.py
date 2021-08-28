from django import forms
from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.urls import reverse
import datetime
from django.utils import timezone


class Chatroom(models.Model):
    cap = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    sub = models.DecimalField(max_digits=1,decimal_places=0,default=0)
    members = models.ManyToManyField(User)

    class Meta:
        ordering = ['-cap']

    def get_members(self):
        return "\n".join([str(m) for m in self.members.all()])

    def get_absolute_url(self):
        return reverse('messages', kwargs={'chat_id': self.pk})

class Message(models.Model):
    chat = models.ForeignKey(Chatroom,verbose_name='Чат',on_delete=models.CASCADE)
    author = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date=models.DateTimeField('Дата сообщения',default=timezone.now)
    is_readed = models.BooleanField('Прочитано',default=False)

    class Meta:
        ordering=['pub_date']
 
    def __str__(self):
        return self.message


class Profile(models.Model):
    TM_CHOICES=[('shTerm','Не длительный'),
                ('lgTerm','Продолжительный')]
    SUB_CHOICES=[
                ('Кировско-Выборгская',(
                        ('1','Девяткино'),
                        ('2','Гражданский проспект'),
                        ('3','Академическая'),
                        ('4','Политехническая'),
                        ('5','Площадь Мужестват'),
                        ('6','Лесная'),
                        ('7','Выборгская'),
                        ('8','Площадь Ленина'),
                        ('9','Чернышевская'),
                        ('10','Площадь Восстания'),
                        ('11','Владимирская'),
                        ('12','Пушкинская'),
                        ('13','Технологический институт'),
                        ('14','Балтийская'),
                        ('15','Нарвская'),
                        ('16','Кировский завод'),
                        ('17','Автово'),
                        ('18','Ленинский проспект'),
                        ('19','Проспект Ветеранов')
                        )
                ),
                ('Московско-Петроградская',(
                        ('20','Парнас'),
                        ('21','Проспект Просвещения'),
                        ('22','Озерки'),
                        ('23','Удельная'),
                        ('24','Пионерская'),
                        ('25','Чёрная речка'),
                        ('26','Петроградская'),
                        ('27','Горьковская'),
                        ('28','Невский проспект'),
                        ('29','Сенная площадь'),
                        ('30','Технологический институт'),
                        ('31','Фрунзенская'),
                        ('32','Московские ворота'),
                        ('33','Электросила'),
                        ('34','Парк Победы'),
                        ('35','Московская'),
                        ('36','Звёздная'),
                        ('37','Купчино')
                        )
                ),
                ('Невско-Василеостровская',(
                        ('38','Беговая'),
                        ('39','Зенит'),
                        ('40','Приморская'),
                        ('41','Василеостровская'),
                        ('42','Гостиный двор'),
                        ('43','Маяковская'),
                        ('44','Площадь Александра Невского'),
                        ('45','Елизаровская'),
                        ('46','Ломоносовская'),
                        ('47','Пролетарская'),
                        ('48','Обухово'),
                        ('49','Рыбацкое')
                        )
                ),
                ('Правобережная',(
                        ('50','Спасская'),
                        ('51','Достоевская'),
                        ('52','Лиговский проспект'),
                        ('53','Площадь Александра Невского'),
                        ('54','Новочеркасская'),
                        ('55','Ладожская'),
                        ('56','Проспект Большевиков'),
                        ('57','Улица Дыбенко')
                        )
                ),
                ('Фрунзенско-Приморская',(
                        ('58','Комендантский проспект'),
                        ('59','Старая Деревня'),
                        ('60','Крестовский остров'),
                        ('61','Чкаловская'),
                        ('62','Спортивная'),
                        ('63','Адмиралтейская'),
                        ('64','Садовая'),
                        ('65','Звенигородская'),
                        ('66','Обводный канал'),
                        ('67','Волковская'),
                        ('68','Бухарестская'),
                        ('69','Международная'),
                        ('70','Проспект Славы'),
                        ('71','Дунайская'),
                        ('72','Шушары')
                        )
                )]
    LST_CHOICES=[('early','Жаворонок'),
                ('something','Когда как'),
                ('late','Сова')]

    COMU_CHOICES=[('intrv','Интроверт'),
                ('extrv','Экстраверт')]

    BADIC_CHOICES=[('smokad','Курю'),
                ('drinad','Пью'),
                ('nodiet','Неправильно питаюсь'),
                ('gamead','Люблю игры'),
                ('lowmov','Малоподвижный образ жизни'),
                ('anotad','Есть другие зависимости'),
                ('noadic','Ничего из этого списка')]

    SOULV_CHOICES=[('lowsou','Люблю тишину'),
                ('midsou','Без разницы'),
                ('nomsou','Люблю громкую музыку')]

    GUESTS_CHOICES=[('noguest','Не люблю гостей'),
                ('hmguest','Нейтрально'),
                ('siguest','Гости это обязательно')]

    COMMUNISM_CHOICES=[('capitalism','У каждого своя еда и посуда'),
                ('idk','Cреднее'),
                ('communism','Можно все общее')]
        
    GENDER_CHOICES=[('man','Мужской'),
                ('inbetween','Не имеет значения'),
                ('woman','Женский')]

    RELIGY_CHOICES=[('сhrist','Христианство'),
                ('muslim','Ислам'),
                ('induism','Индуизм'),
                ('budism','Будизм'),
                ('iudaism','Иудаизм'),
                ('pastafarian','Пастафарианство'),
                ('ateism','Я считаю себя атеистом'),
                ('nosing','Это не имеет значения')]
    
    FRETIM_CHOICES=[('cafe','Кафе'),
                ('socnet','Соц.сети'),
                ('drinkin','Выпивка'),
                ('cinema','Кинотеатр'),
                ('culture','Культурные места: театры, выставки, музеи и т.д'),
                ('reading','Чтение'),
                ('activity','Активный отдых'),
                ('imprusf','Развитие себя'),
                ('games','Игры'),
                ('study','Учеба')]

    PETS_CHOICES=[('si','У меня есть питомец'),
                ('nomater','Мне без разницы'),
                ('no','Я против любой живности')]

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    urAge= models.DecimalField(max_digits=2,decimal_places=0,default=18,verbose_name="Возраст:")
    rmAgeL= models.DecimalField(max_digits=2,decimal_places=0,default=18,verbose_name="От:")
    rmAgeU= models.DecimalField(max_digits=2,decimal_places=0,default=18,verbose_name="До:")

#Аренда
    rntLPrice = models.DecimalField(max_digits=5,decimal_places=0,default=10000,verbose_name="От:")
    rntUPrice = models.DecimalField(max_digits=5,decimal_places=0,default=15000,verbose_name="До:")
    rntTime = models.CharField(max_length=15, choices=TM_CHOICES, default='lgTerm',verbose_name="Срок аренды:")
    rntSubway = MultiSelectField( choices=SUB_CHOICES, default='0',verbose_name="Станции метро:")
#О тебе
    abuLST = models.CharField(max_length=15,choices=LST_CHOICES,default='early',verbose_name='Хронотип:')
    abuCOMU = models.CharField(max_length=10,choices=COMU_CHOICES,default='intrv',verbose_name='Темперамент:')
    abuBADIC = MultiSelectField(choices=BADIC_CHOICES,verbose_name="Вредные привычки:")
    abuORGL = models.DecimalField(max_digits=2,decimal_places=0,default=5,verbose_name="Уровень организованности (0-10):")
#О помещении
    abrTEMP = models.DecimalField(max_digits=2,decimal_places=0,default=24,verbose_name="Комфортная температура:")
    abrSOUL = models.CharField(max_length=25,choices=SOULV_CHOICES,default='midsou',verbose_name='Общий уровень шума:')
    abrCLEAN = models.DecimalField(max_digits=2,decimal_places=0,default=8,verbose_name="Кол-во уборок в месяц (0-30):")
    abrGUEST = models.CharField(max_length=25,choices=GUESTS_CHOICES,default='hmguest',verbose_name='Отношение к гостям:')
    abrCOMMUNISM = models.CharField(max_length=30,choices=COMMUNISM_CHOICES,default='idk',verbose_name='Отношение к быту:')
#О предпочтениях
    aprUGEN=models.CharField(max_length=20,choices=GENDER_CHOICES,default='inbetween',verbose_name='Пол:')
    aprR8GEN=models.CharField(max_length=20,choices=GENDER_CHOICES,default='inbetween',verbose_name='Пол:')
    aprURRELIGY=models.CharField(max_length=25,choices=RELIGY_CHOICES,default='pastafarian',verbose_name='Религия:')
    aprR8RELIGY=models.CharField(max_length=25,choices=RELIGY_CHOICES,default='pastafarian',verbose_name='Религия:')
    aprFRETM = MultiSelectField( choices=FRETIM_CHOICES,verbose_name="Cвободное время:")
    aprPETS = models.CharField(max_length=15,choices=PETS_CHOICES,default='nomater',verbose_name='Питомцы допустимы?')
    aprTELLUS = models.TextField(max_length=160,default='Мне было лень это менять.',verbose_name='Пара слов о тебе (160 символов):')

    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True,verbose_name='Тут можно загрузить свое фото', default='users/profdef.svg')

    contInsta = models.CharField(max_length=60,default="",blank=True)
    contTeleg = models.CharField(max_length=60,default="",blank=True)
    contVKont = models.CharField(max_length=60,default="",blank=True)

    mesNotif= models.BooleanField(default=True,verbose_name='Уведомлять меня о новых сообщения:')
    chatNotif= models.BooleanField(default=True,verbose_name='Уведомлять меня о новых соседях:')
    active= models.BooleanField(default=False)
    last_activity=models.DateField(max_length=150,default=timezone.now,blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
# Create your models here.
