from django.db.models import (Model,
                              CharField,
                              DecimalField,
                              IntegerField,
                              TextField,
                              BooleanField,
                              ManyToManyField)

# Create your models here.
class Buyer(Model):
    name = CharField(max_length=100)
    balance = DecimalField(decimal_places=2, max_digits=5)
    age = IntegerField()


class Game(Model):
    title = CharField(max_length=100)
    cost = DecimalField(decimal_places=2, max_digits=5)
    size = DecimalField(decimal_places=2, max_digits=5)
    description = TextField()
    age_limited = BooleanField()
    buyer = ManyToManyField(Buyer, related_name='games')