from django.db import models

# Create your models here.
class Ing(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return f'{self.name}'

class Drink(models.Model):
    name = models.CharField(max_length=255)
    glassType = models.CharField(max_length=50)
    recipe= models.TextField()
    ing = models.ManyToManyField(Ing, through='Amount', through_fields=('drink', 'ing'))
    def __repr__(self):
        return f'{self.name}'


class Amount(models.Model):
    drink = models.ForeignKey(Drink)
    ing = models.ForeignKey(Ing)
    amount = models.CharField(max_length=10)