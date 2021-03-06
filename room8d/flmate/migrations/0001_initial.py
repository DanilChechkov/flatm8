# Generated by Django 3.2.4 on 2021-06-04 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cap', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('sub', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-cap'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urAge', models.DecimalField(decimal_places=0, default=18, max_digits=2, verbose_name='Возраст:')),
                ('rmAgeL', models.DecimalField(decimal_places=0, default=18, max_digits=2, verbose_name='Возраст соседа от:')),
                ('rmAgeU', models.DecimalField(decimal_places=0, default=18, max_digits=2, verbose_name='До:')),
                ('rntLPrice', models.DecimalField(decimal_places=0, default=10000, max_digits=5, verbose_name='Минимальная цена за всю квартиру:')),
                ('rntUPrice', models.DecimalField(decimal_places=0, default=15000, max_digits=5, verbose_name='Максимальная цена за всю квартиру:')),
                ('rntTime', models.CharField(choices=[('shTerm', 'Не длительный'), ('lgTerm', 'Продолжительный')], default='lgTerm', max_length=15, verbose_name='Срок аренды:')),
                ('rntSubway', multiselectfield.db.fields.MultiSelectField(choices=[('Кировско-Выборгская', (('1', 'Девяткино'), ('2', 'Гражданский проспект'), ('3', 'Академическая'), ('4', 'Политехническая'), ('5', 'Площадь Мужестват'), ('6', 'Лесная'), ('7', 'Выборгская'), ('8', 'Площадь Ленина'), ('9', 'Чернышевская'), ('10', 'Площадь Восстания'), ('11', 'Владимирская'), ('12', 'Пушкинская'), ('13', 'Технологический институт'), ('14', 'Балтийская'), ('15', 'Нарвская'), ('16', 'Кировский завод'), ('17', 'Автово'), ('18', 'Ленинский проспект'), ('19', 'Проспект Ветеранов'))), ('Московско-Петроградская', (('20', 'Парнас'), ('21', 'Проспект Просвещения'), ('22', 'Озерки'), ('23', 'Удельная'), ('24', 'Пионерская'), ('25', 'Чёрная речка'), ('26', 'Петроградская'), ('27', 'Горьковская'), ('28', 'Невский проспект'), ('29', 'Сенная площадь'), ('30', 'Технологический институт'), ('31', 'Фрунзенская'), ('32', 'Московские ворота'), ('33', 'Электросила'), ('34', 'Парк Победы'), ('35', 'Московская'), ('36', 'Звёздная'), ('37', 'Купчино'))), ('Невско-Василеостровская', (('38', 'Беговая'), ('39', 'Зенит'), ('40', 'Приморская'), ('41', 'Василеостровская'), ('42', 'Гостиный двор'), ('43', 'Маяковская'), ('44', 'Площадь Александра Невского'), ('45', 'Елизаровская'), ('46', 'Ломоносовская'), ('47', 'Пролетарская'), ('48', 'Обухово'), ('49', 'Рыбацкое'))), ('Правобережная', (('50', 'Спасская'), ('51', 'Достоевская'), ('52', 'Лиговский проспект'), ('53', 'Площадь Александра Невского'), ('54', 'Новочеркасская'), ('55', 'Ладожская'), ('56', 'Проспект Большевиков'), ('57', 'Улица Дыбенко'))), ('Фрунзенско-Приморская', (('58', 'Комендантский проспект'), ('59', 'Старая Деревня'), ('60', 'Крестовский остров'), ('61', 'Чкаловская'), ('62', 'Спортивная'), ('63', 'Адмиралтейская'), ('64', 'Садовая'), ('65', 'Звенигородская'), ('66', 'Обводный канал'), ('67', 'Волковская'), ('68', 'Бухарестская'), ('69', 'Международная'), ('70', 'Проспект Славы'), ('71', 'Дунайская'), ('72', 'Шушары')))], default='0', max_length=103, verbose_name='Станция метро:')),
                ('abuLST', models.CharField(choices=[('early', 'Жаворонок'), ('something', 'Когда как'), ('late', 'Сова')], default='early', max_length=15, verbose_name='Хронотип:')),
                ('abuCOMU', models.CharField(choices=[('intrv', 'Интроверт'), ('extrv', 'Экстраверт')], default='intrv', max_length=10, verbose_name='Темперамент:')),
                ('abuBADIC', multiselectfield.db.fields.MultiSelectField(choices=[('smokad', 'Курю'), ('drinad', 'Пью'), ('nodiet', 'Неправильно питаюсь'), ('gamead', 'Люблю игры'), ('lowmov', 'Малоподвижный образ жизни'), ('anotad', 'Есть другие зависимости'), ('noadic', 'Ничего из этого списка')], default='noadic', max_length=48, verbose_name='Вредные привычки:')),
                ('abuORGL', models.DecimalField(decimal_places=0, default=50, max_digits=2, verbose_name='Уровень организованности (0-10):')),
                ('abrTEMP', models.DecimalField(decimal_places=0, default=24, max_digits=2, verbose_name='Комфортная температура:')),
                ('abrSOUL', models.CharField(choices=[('lowsou', 'Люблю тишину'), ('midsou', 'Без разницы'), ('nomsou', 'Люблю громкую музыку')], default='midsou', max_length=25, verbose_name='Общий уровень шума:')),
                ('abrCLEAN', models.DecimalField(decimal_places=0, default=8, max_digits=2, verbose_name='Сколько раз в месяц убираешься (0-30):')),
                ('abrGUEST', models.CharField(choices=[('noguest', 'Не люблю гостей'), ('hmguest', 'Нейтрально'), ('siguest', 'Гости это обязательно')], default='hmguest', max_length=25, verbose_name='Отношение к гостям:')),
                ('abrCOMMUNISM', models.CharField(choices=[('capitalism', 'У каждого своя еда и посуда'), ('idk', 'Cреднее'), ('communism', 'Можно все общее')], default='idk', max_length=30, verbose_name='Отношение к быту:')),
                ('aprUGEN', models.CharField(choices=[('man', 'Мужской'), ('inbetween', 'Не имеет значения'), ('woman', 'Женский')], default='inbetween', max_length=20, verbose_name='Пол:')),
                ('aprR8GEN', models.CharField(choices=[('man', 'Мужской'), ('inbetween', 'Не имеет значения'), ('woman', 'Женский')], default='inbetween', max_length=20, verbose_name='Пол соседа:')),
                ('aprURRELIGY', models.CharField(choices=[('сhrist', 'Христианство'), ('muslim', 'Ислам'), ('induism', 'Индуизм'), ('budism', 'Будизм'), ('iudaism', 'Иудаизм'), ('pastafarian', 'Пастафарианство'), ('ateism', 'Я считаю себя атеистом'), ('nosing', 'Это не имеет значения')], default='pastafarian', max_length=25, verbose_name='Религия:')),
                ('aprR8RELIGY', models.CharField(choices=[('сhrist', 'Христианство'), ('muslim', 'Ислам'), ('induism', 'Индуизм'), ('budism', 'Будизм'), ('iudaism', 'Иудаизм'), ('pastafarian', 'Пастафарианство'), ('ateism', 'Я считаю себя атеистом'), ('nosing', 'Это не имеет значения')], default='pastafarian', max_length=25, verbose_name='Религия соседа:')),
                ('aprFRETM', multiselectfield.db.fields.MultiSelectField(choices=[('cafe', 'Кафе'), ('socnet', 'Соц.сети'), ('drinkin', 'Выпивка'), ('cinema', 'Кинотеатр'), ('culture', 'Культурные места: театры, выставки, музеи и т.д'), ('reading', 'Чтение'), ('activity', 'Активный отдых'), ('imprusf', 'Развитие себя'), ('games', 'Игры'), ('study', 'Учеба')], default='imprusf', max_length=71, verbose_name='Как проводишь свободное время:')),
                ('aprPETS', models.CharField(choices=[('si', 'У меня есть питомец'), ('nomater', 'Мне без разницы'), ('no', 'Я против любой живности')], default='nomater', max_length=15, verbose_name='Питомцы допустимы?')),
                ('aprTELLUS', models.TextField(default='Мне было лень это менять.', max_length=160, verbose_name='Пара слов о тебе (160 символов):')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='Тут можно загрузить свое фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flmate.chatroom', verbose_name='Чат')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
