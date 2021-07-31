from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    message= models.CharField(max_length=500)


class Carousel(models.Model):
    image= models.ImageField(upload_to='img')
    title=models.CharField(max_length=150)
    sub_title=models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title=models.CharField(max_length=200,blank=True)
    url_field=models.CharField(max_length=200,blank=True)
  
class SubMenu(models.Model):
    title=models.CharField(max_length=200,blank=True)
    url_field=models.CharField(max_length=200,blank=True)

class Logo(models.Model):
    logo= models.ImageField(upload_to='logo',blank=True)
     