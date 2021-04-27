from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

import random

class roles(models.Model):
    """ 
    Team members roles
    """   
    name = models.CharField(max_length=511,unique=True)

    created_by = models.CharField(max_length=511,null=True,blank=True , default = "default")

    created = models.DateTimeField(editable=False)

    description = models.TextField(null=True,blank=True)
    
    modified = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(roles, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-modified' ,)
        db_table = 'accounts_role'



class team_member(models.Model):
    """ 
    Base team member model 
    """
    user = models.ForeignKey(User, unique=False ,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=511, unique=False, null =True, blank = True)

    role = models.ForeignKey(roles, unique=False, on_delete=models.DO_NOTHING)

    created_by = models.CharField(max_length=511, unique=False, null =True, blank = True, default="default")

    created = models.DateTimeField(editable=False)
    
    modified = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps & gen uuid on creation'''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(team_member, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-modified' ,)