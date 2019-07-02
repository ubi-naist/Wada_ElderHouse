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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.uid, self.uname, self.gender,
        self.age, self.height, self.weight, self.created_at, self.updated_at)

class Area(models.Model):
    areaid = models.UUIDField()
    areaname = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {} {} {}'.format(self.areaid, self.areaname, self.created_at, self.updated_at)

class Beacon(models.Model):
    bid = models.UUIDField()
    uuid = models.UUIDField()
    major = models.IntegerField()
    minor = models.IntegerField()
    type = models.CharField(max_length=20)
    typeid = models.UUIDField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.bid, self.uuid, self.major,self.minor,
            self.type, self.typeid, self.created_at, self.updated_at)

class Record(models.Model):
    rid = models.UUIDField()
    sid = models.UUIDField()
    uid = models.UUIDField()
    areaid = models.UUIDField()
    cid = models.UUIDField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.rid, self.sid, self.uid, self.areaid,
         self.cid, self.created_at, self.updated_at)

class CareType(models.Model):
    careid = models.UUIDField()
    careType = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.careid, self.careType)

class ToiletRecord(models.Model):
    toilet_id = models.UUIDField()
    toilet_status = models.CharField(max_length=30)
    toilet_amount = models.CharField(max_length=30)

    def __str__(self):
        return '{} {} {}'.format(self.toilet_id, self.toilet_status, self.toilet_amount)

class BathRecord(models.Model):
    bath_id = models.UUIDField()
    bath_medicine = models.CharField(max_length=30)
    bath_status = models.CharField(max_length=30)

    def __str__(self):
        return '{} {} {}'.format(self.bath_id, self.bath_medicine, self.bath_status)
