from django.db import models
from django.utils.text import slugify

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    phone = models.IntegerField(null = True)
    joined_date = models.DateField(null = True)
    slug = models.SlugField(default="",null = False)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.firstname}-{self.lastname}")
        super(Member, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class User(models.Model):
    email = models.CharField(primary_key= True,max_length = 20 )
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.user_name
    
class Topic(models.Model):
    id_topic = models.IntegerField(primary_key= True,null = False)
    name_topic = models.CharField(max_length = 30, blank = False)
    email = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.name_topic
    
class Flashcard(models.Model):
    id_flashcard = models.IntegerField(primary_key = True, null = False)
    front = models.CharField(max_length = 30, blank = False)
    back = models.CharField(max_length = 50, blank = False)
    count = models.IntegerField(null = False)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.front

class Process(models.Model):
    id_prodess  = models.IntegerField(primary_key = True, null = False)
    time_login = models.DateField()
    number_time_study = models.DurationField()
    email = models.ForeignKey(User, on_delete=models.CASCADE)
