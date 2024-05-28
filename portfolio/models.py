from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=15,null=True)

    def __str__(self) -> str:
        return self.name


class Details(models.Model):
    #user = models.ForeignKey(User , on_delete=models.CASCADE)   #on_delete = models.CASCADE or .SET_NULL or SET_DEFAULT 
    id = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=30)                              # if user delete the user related data will delete
    phone = models.CharField(max_length=15)
    class_name = models.CharField(max_length=10,default='SOME STRING')
    fee_due = models.IntegerField(default=1000)
    school = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='course',null=True,blank=True)

    def __str__(self):
        return self.id

class Questions(models.Model):
    question = models.CharField(max_length=2000)
    option1 = models.CharField(max_length = 200)
    option2 = models.CharField(max_length = 200)
    option3 = models.CharField(max_length = 200)
    option4 = models.CharField(max_length = 200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Marks(models.Model):
    std_id = models.OneToOneField(Details,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.std_id)

    

@receiver(post_save, sender=Details)
def create_marks(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Marks.objects.create(std_id=instance)











