from django.db import models
from django.contrib.auth.models import User

# class AllUsers(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length = 254)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username

class DeepUserDetails(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    reputation = models.PositiveIntegerField()
    totalupvote = models.PositiveIntegerField()
    totaldownvote = models.PositiveIntegerField()
    totaltips = models.PositiveIntegerField()

    def __str__(self):
        return u'%s - %d' % (self.userid.username,self.reputation)

class Tips(models.Model):
    userid = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    tags = models.CharField(max_length=50)
    comment = models.CharField(max_length=5000,blank=True,null=True)
    links = models.CharField(max_length=5000,blank=True,null=True)
    file =  models.FileField(upload_to='files/', null=True, verbose_name="")
    date = models.DateTimeField(auto_now=True)
    upvote = models.PositiveIntegerField()
    downvote = models.PositiveIntegerField()
    totalscore = models.IntegerField()