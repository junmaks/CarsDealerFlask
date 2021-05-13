from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField
from config import DB_NAME
import datetime

cars_dealers_db = SqliteDatabase(DB_NAME, pragmas={'foreign_keys': 1})


class Dealers(Model):
    class Meta:
        database = cars_dealers_db
        order_by = ('year')

    title = CharField(max_length=100, verbose_name='Name of organisation')
    locations = CharField(max_length=255, verbose_name='Location')
    year = IntegerField(verbose_name='Foundation date ')


class Cars(Model):
    class Meta:
        database = cars_dealers_db
        order_by = ('year_release')
    brand = CharField(max_length=100, verbose_name='Brand')
    car_model = CharField(max_length=100, verbose_name='Model')
    year_release = IntegerField(default=datetime.date.today().year, verbose_name='Year')
    price = IntegerField(verbose_name='Price')
    dealer = ForeignKeyField(model=Dealers, related_name='cars', on_delete='CASCADE')


Dealers.create_table(True)
Cars.create_table(True)