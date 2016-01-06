from __future__ import unicode_literals

from django.db import transaction
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'))
    phone = models.CharField(max_length=20)
    
    USER_SOURCE = (
        ('LO', 'Local'),
        ('WB', 'Weibo'),
        ('QQ', 'QQ'),
    )
    source = models.CharField(max_length=2, choices=USER_SOURCE, default='LO')
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    
    @transaction.atomic
    def createUser(self):
        self.user.save()
        self.save()