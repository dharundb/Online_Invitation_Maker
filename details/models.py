from django.db import models
from django.db.models.fields import TimeField

# Create your models here.
class wed_credential(models.Model):
    groom = models.CharField(max_length=64)
    bride = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    date = models.DateField()
    occasion = models.CharField(max_length=64)
    time = models.TimeField()

    def __str__(self): 
        return f'{self.id} -> Occasion : Wedding || Groom : {self.groom}  ||  Bride : {self.bride}  ||  Address : {self.address} || Contact : {self.contact} || Date : {self.date} || Time : {self.time}'

class gath_credential(models.Model):
    occasion = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.id} -> Occasion : {self.occasion} ||  Address : {self.address} || Contact : {self.contact} || Date : {self.date} || Time : {self.time}'

class bday_credential(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    date = models.DateField()
    occasion = models.CharField(max_length=64)
    age = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.id} -> Occasion : {self.occasion} || Name : {self.name}  || Age : {self.age} || Address : {self.address} || Contact : {self.contact} || Date : {self.date} || Time : {self.time}'

class Media(models.Model):
    pic = models.ImageField(null=True, blank=True)
    pic_url = models.CharField(max_length=64)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.tag} -> {self.pic_url}'
