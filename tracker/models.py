from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class IP(models.Model):
    ip = models.CharField(max_length=32)

    def  __unicode__(self):
        return self.ip


class Port(models.Model):
    port_no = models.IntegerField()






class MobileReg(models.Model):
    choice =  ((True,'ON'), (False, 'OFF'))
    choice2 = ((True, 'START'), (False, 'STOP'))
    choice3 = ((True, 'Alert ON'),(False, 'Dont Alert'))

    mobile_id = models.CharField(default=000,max_length=3,blank=True)
    mobile_no =  models.CharField(max_length=12,null=True)
    device_id = models.CharField(max_length= 8,null=True)
    eng_notify   = models.NullBooleanField(choices=choice,default=False)
    ac_notify = models.NullBooleanField(choices=choice,default=False)
    door_notify = models.NullBooleanField(choices=choice,default=False)
    status_notify = models.NullBooleanField(choices=choice2,default=False)
    fuel_notify = models.NullBooleanField(choices=choice,default=False)
    speed_notify = models.NullBooleanField(choices=choice,default=False)
    where_notify = models.NullBooleanField(choices=choice,default=False)

    departure_alert = models.NullBooleanField(choices=choice3, default=False)
    eng_alert = models.NullBooleanField(choices=choice3, default=False)
    ac_alert = models.NullBooleanField(choices=choice3, default=False)
    door_alert = models.NullBooleanField(choices=choice3, default=False)
    arrival_alert = models.NullBooleanField(choices=choice3, default=False)
    fuel_alert = models.NullBooleanField(choices=choice3, default=False)
    speed_alert = models.NullBooleanField(choices=choice3, default=False)
    radius_alert = models.NullBooleanField(choices=choice3, default=False)

    departure_enable = models.NullBooleanField(choices=choice, default=False)
    eng_enable = models.NullBooleanField(choices=choice, default=False)
    ac_enable = models.NullBooleanField(choices=choice, default=False)
    door_enable = models.NullBooleanField(choices=choice, default=False)
    arrival_enable = models.NullBooleanField(choices=choice, default=False)
    fuel_enable = models.NullBooleanField(choices=choice, default=False)
    speed_enable = models.NullBooleanField(choices=choice, default=False)
    radius_enable = models.NullBooleanField(choices=choice, default=False)

    lat = models.FloatField(default=0.0000)
    lng = models.FloatField(default=0.0000)
    radius = models.CharField(max_length=5)
    speed = models.CharField(max_length=3)

    def __unicode__(self):
        return self.mobile_no


class AddDevice(models.Model):
    user = models.ForeignKey(User)
    device_id = models.CharField(max_length=8)
    imei = models.CharField(max_length=15,null=True)
    mobile_no = models.CharField(max_length=12)
    ip = models.ForeignKey(IP,null=True)
    port = models.ForeignKey(Port,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __unicode__(self):
        return self.device_id



class Notify(models.Model):
    device_id = models.CharField(max_length=8)
    mobile_no  = models.CharField(max_length=12)
    notify_type = models.IntegerField()
    notify_result = models.CharField(max_length=80)

    def __unicode__(self):
        return self.mobile_no



class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Reseller = models.NullBooleanField(default=False,null=True)