from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class sc_list(models.Model):
    sc_name = models.CharField(max_length=32)
    sc_address = models.CharField(max_length=32)
    sc_manager = models.CharField(max_length=32)
    sc_phone = models.CharField(max_length=32)
    dk_num = models.IntegerField(default=0)
    ctime = models.DateField(auto_now_add=True, null=True)
    uptime = models.DateField(auto_now=True, null=True)


class store_list(models.Model):
    sc = models.ForeignKey(sc_list,on_delete=models.CASCADE)
    floor = models.CharField(max_length=32)
    store_order = models.CharField(max_length=32)
