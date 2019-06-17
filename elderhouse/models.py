import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Elder(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=70)

    def __str__(self):
        return self.name

class Staff(models.Model):
    sid = models.UUIDField()
    sname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    device_name = models.CharField(max_length=20)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.sid, self.sname, self.gender,
        self.age, self.created_at, self.updated_at, self.device_name)

class Resident(models.Model):
    uid = models.UUIDField()
    uname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.uid, self.uname, self.gender,
        self.age, self.height, self.weight, self.created_at, self.updated_at)

class Area(models.Model):
    areaid = models.UUIDField()
    areaname = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{} {} {} {}'.format(self.areaid, self.areaname, self.created_at, self.updated_at)

class Beacon(models.Model):
    bid = models.UUIDField()
    uuid = models.UUIDField()
    major = models.IntegerField()
    minor = models.IntegerField()
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())


        def __str__(self):
            return '{} {} {} {} {} {} {}'.format(self.bid, self.uuid, self.major,self.minor,
            self.type, self.created_at, self.updated_at)
