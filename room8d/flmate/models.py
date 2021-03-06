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
    CITY_CHOICES=[('spb','Санкт-Петербург'),
                ('msc','Москва')]
    SPBSUB_CHOICES=[
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
                    )
                ]
    MSCSUB_CHOICES=[
                    ('Сокольническая',(
                        ('1','Бульвар Рокоссовского'),
                        ('2','Черкизовская'),
                        ('3','Преображенская площадь'),
                        ('4','Сокольники'),
                        ('5','Красносельская'),
                        ('6','Комсомольская'),
                        ('7','Красные Ворота'),
                        ('8','Чистые пруды'),
                        ('9','Лубянка'),
                        ('10','Охотный Ряд'),
                        ('11','Библиотека имени Ленина'),
                        ('12','Кропоткинская'),
                        ('13','Парк культуры'),
                        ('14','Фрунзенская'),
                        ('15','Спортивная'),
                        ('16','Воробьёвы горы'),
                        ('17','Университет'),
                        ('18','Проспект Вернадского'),
                        ('19','Юго-Западная'),
                        ('20','Тропарёво'),
                        ('21','Румянцево'),
                        ('22','Саларьево'),
                        ('23','Филатов Луг'),
                        ('24','Прокшино'),
                        ('25','Ольховая'),
                        ('26','Коммунарка')
                        )),
                    ('Замоскворецкая',(
                        ('27','Ховрино'),
                        ('28','Беломорская'),
                        ('29','Речной вокзал'),
                        ('30','Водный стадион'),
                        ('31','Войковская'),
                        ('32','Сокол'),
                        ('33','Аэропорт'),
                        ('34','Динамо'),
                        ('35','Белорусская'),
                        ('36','Маяковская'),
                        ('37','Тверская'),
                        ('38','Театральная'),
                        ('39','Новокузнецкая'),
                        ('40','Павелецкая'),
                        ('41','Автозаводская'),
                        ('42','Технопарк'),
                        ('43','Коломенская'),
                        ('44','Каширская'),
                        ('45','Кантемировская'),
                        ('46','Царицыно'),
                        ('47','Орехово'),
                        ('48','Домодедовская'),
                        ('49','Красногвардейская'),
                        ('50','Алма-Атинская')
                        )),
                    ('Арбатско-Покровская',(
                        ('51','Пятницкое шоссе'),
                        ('52','Митино'),
                        ('53','Волоколамская'),
                        ('54','Мякинино'),
                        ('55','Строгино'),
                        ('56','Крылатское'),
                        ('57','Молодёжная'),
                        ('58','Кунцевская'),
                        ('59','Славянский бульвар'),
                        ('60','Парк Победы'),
                        ('61','Киевская'),
                        ('62','Смоленская'),
                        ('63','Арбатская'),
                        ('64','Площадь Революции'),
                        ('65','Курская'),
                        ('66','Бауманская'),
                        ('67','Электрозаводская'),
                        ('68','Семёновская'),
                        ('69','Партизанская'),
                        ('70','Измайловская'),
                        ('71','Первомайская'),
                        ('72','Щёлковская')
                        )),
                    ('Филёвская',(
                        ('73','Кунцевская'),
                        ('74','Пионерская'),
                        ('75','Филёвский парк'),
                        ('76','Багратионовская'),
                        ('77','Фили'),
                        ('78','Кутузовская'),
                        ('79','Студенческая'),
                        ('80','Международная'),
                        ('81','Выставочная'),
                        ('82','Киевская'),
                        ('83','Смоленская'),
                        ('84','Арбатская'),
                        ('85','Александровский сад')
                        )),
                    ('Кольцевая',(
                        ('86','Парк культуры'),
                        ('87','Октябрьская'),
                        ('88','Добрынинская'),
                        ('89','Павелецкая'),
                        ('90','Таганская'),
                        ('91','Курская'),
                        ('92','Комсомольская'),
                        ('93','Проспект Мира'),
                        ('94','Новослободская'),
                        ('95','Белорусская'),
                        ('96','Краснопресненская'),
                        ('97','Киевская')
                        )),
                    ('Калужско-Рижская',(
                        ('98','Медведково'),
                        ('99','Бабушкинская'),
                        ('100','Свиблово'),
                        ('101','Ботанический сад'),
                        ('102','ВДНХ'),
                        ('103','Алексеевская'),
                        ('104','Рижская'),
                        ('105','Проспект Мира'),
                        ('106','Сухаревская'),
                        ('107','Тургеневская'),
                        ('108','Китай-город'),
                        ('109','Третьяковская'),
                        ('109','Октябрьская'),
                        ('109','Шаболовская'),
                        ('109','Ленинский проспект'),
                        ('109','Академическая'),
                        ('109','Профсоюзная'),
                        ('109','Новые Черёмушки'),
                        ('109','Калужская'),
                        ('109','Беляево'),
                        ('109','Коньково'),
                        ('109','Тёплый Стан'),
                        ('109','Ясенево'),
                        ('109','Новоясеневская')
                        )),
                    ('Таганско-Краснопресненская',(
                        ('110','Планерная'),
                        ('111','Сходненская'),
                        ('112','Тушинская'),
                        ('113','Спартак'),
                        ('114','Щукинская'),
                        ('115','Октябрьское Поле'),
                        ('116','Полежаевская'),
                        ('117','Беговая'),
                        ('118','Улица 1905 года'),
                        ('119','Баррикадная'),
                        ('120','Пушкинская'),
                        ('121','Кузнецкий Мост'),
                        ('122','Китай-город'),
                        ('123','Таганская'),
                        ('124','Пролетарская'),
                        ('125','Волгоградский проспект'),
                        ('126','Текстильщики'),
                        ('127','Кузьминки'),
                        ('128','Рязанский проспект'),
                        ('129','Выхино'),
                        ('130','Лермонтовский проспект'),
                        ('131','Жулебино'),
                        ('132','Котельники')
                        )),
                    ('Калининская',(
                        ('133','Третьяковская'),
                        ('134','Марксистская'),
                        ('135','Площадь Ильича'),
                        ('136','Авиамоторная'),
                        ('137','Шоссе Энтузиастов'),
                        ('138','Перово'),
                        ('139','Новогиреево'),
                        ('140','Новокосино'),
                        ('141','Рассказовка'),
                        ('142','Новопеределкино'),
                        ('143','Боровское шоссе'),
                        ('144','Солнцево'),
                        ('145','Говорово'),
                        ('146','Озёрная'),
                        ('147','Мичуринский проспект'),
                        ('148','Раменки'),
                        ('149','Ломоносовский проспект'),
                        ('150','Минская'),
                        ('151','Парк Победы'),
                        ('152','Деловой центр')
                        )),
                    ('Серпуховско-Тимирязевская',(
                        ('153','Алтуфьево'),
                        ('154','Бибирево'),
                        ('155','Отрадное'),
                        ('156','Владыкино'),
                        ('157','Петровско-Разумовская'),
                        ('158','Тимирязевская'),
                        ('159','Дмитровская'),
                        ('160','Савёловская'),
                        ('161','Менделеевская'),
                        ('162','Цветной бульвар'),
                        ('163','Чеховская'),
                        ('164','Боровицкая'),
                        ('165','Полянка'),
                        ('166','Серпуховская'),
                        ('167','Тульская'),
                        ('168','Нагатинская'),
                        ('169','Нагорная'),
                        ('170','Нахимовский проспект'),
                        ('171','Севастопольская'),
                        ('172','Чертановская'),
                        ('173','Южная'),
                        ('174','Пражская'),
                        ('175','Улица Академика Янгеля'),
                        ('176','Аннино'),
                        ('177','Бульвар Дмитрия Донского')
                        )),
                    ('Любли́нско-Дми́тровская',(
                        ('178','Селигерская'),
                        ('179','Верхние Лихоборы'),
                        ('180','Окружная'),
                        ('181','Петровско-Разумовская'),
                        ('182','Фонвизинская'),
                        ('183','Бутырская'),
                        ('184','Марьина Роща'),
                        ('185','Достоевская'),
                        ('186','Трубная'),
                        ('187','Сретенский бульвар'),
                        ('188','Чкаловская'),
                        ('189','Римская'),
                        ('190','Крестьянская застава'),
                        ('191','Дубровка'),
                        ('192','Кожуховская'),
                        ('193','Печатники'),
                        ('194','Волжская'),
                        ('195','Люблино'),
                        ('196','Братиславская'),
                        ('197','Марьино'),
                        ('198','Борисово'),
                        ('199','Шипиловская'),
                        ('200','Зябликово')
                        )),
                    ('Большая Кольцевая',(
                        ('201','Деловой центр'),
                        ('202','Шелепиха'),
                        ('203','Мнёвники'),
                        ('204','Народное Ополчение'),
                        ('205','Хорошёвская'),
                        ('206','ЦСКА'),
                        ('207','Петровский парк'),
                        ('208','Савёловская'),
                        ('209','Каширская'),
                        ('210','Варшавская'),
                        ('211','Каховская')
                        )),
                    ('Бутовская',(
                        ('212','Битцевский парк'),
                        ('213','Лесопарковая'),
                        ('214','Улица Старокачаловская'),
                        ('215','Улица Скобелевская'),
                        ('216','Бульвар Адмирала Ушакова'),
                        ('217','Улица Горчакова'),
                        ('218','Бунинская аллея')
                        )),
                    ('Некрасовская',(
                        ('219','Электрозаводская'),
                        ('220','Лефортово'),
                        ('221','Авиамоторная'),
                        ('222','Нижегородская'),
                        ('223','Стахановская'),
                        ('224','Окская'),
                        ('225','Юго-Восточная'),
                        ('226','Косино'),
                        ('227','Улица Дмитриевского'),
                        ('228','Лухмановская'),
                        ('229','Некрасовка')
                        )),
                    ]

    
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
    rntCity = models.CharField(max_length=20,choices=CITY_CHOICES,default='spb',verbose_name='Город:')
    rntSubway = MultiSelectField(choices=SPBSUB_CHOICES, default='0',verbose_name="Станции метро:",blank=True)
    rntSubwayM = MultiSelectField(choices=MSCSUB_CHOICES, default='0',verbose_name="Станции метро:",blank=True)
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
