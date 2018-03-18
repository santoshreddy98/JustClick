from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    qualif = models.CharField(max_length=200)
    category = models.CharField(max_length=150,default='')
    description = models.TextField(max_length=255)
    phone = PhoneNumberField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# class Profile(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
#     name = models.CharField(max_length=100)
#     category = models.ManyToManyField(Category,related_name='category')
#     qualification = models.CharField(max_length=150)
#     des = models.TextField(max_length=200)
#     phone = PhoneNumberField()
#
#     def __str__(self):
#         return self.name
