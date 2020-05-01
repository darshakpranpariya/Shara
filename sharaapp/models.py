from django.db import models
from django.contrib.auth.models import User

class AllUsers(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class DeepUserDetails(models.Model):
    userid = models.ForeignKey(AllUsers,on_delete=models.CASCADE)
    reputation = models.PositiveIntegerField()
    totalupvote = models.PositiveIntegerField()
    totaldownvote = models.PositiveIntegerField()
    totaltips = models.PositiveIntegerField()

    def __str__(self):
        return u'%s - %d' % (self.userid.username,self.reputation)

