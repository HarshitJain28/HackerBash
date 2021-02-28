from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



# Create your models here.


class User(AbstractUser):
    is_consumer = models.BooleanField('consumer status', default=False)
    is_serviceProvider = models.BooleanField('serviceProvider status', default=False)
    first_name = models.CharField(max_length=50,default=' ')
    last_name = models.CharField(max_length=50,default=' ')
    phone_number = models.CharField(max_length=12,default=' ')
    email = models.EmailField()
    address = models.TextField(default=' ')
    locality = models.CharField(max_length=100,default=' ')   
    state = models.CharField(max_length=50,default=' ') 
    city = models.CharField(max_length=50,default=' ')

    # def __str__(self):
    #     return self.first_name 

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

    def __str__(self):
        return self.user.username
    


class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    service_name = models.CharField(max_length=100,default=' ')
    company_name = models.CharField(max_length=100,default='')
    service_picture = models.ImageField(default='default.jpeg', upload_to='service_pics',null=True, blank=True)

    def __str__(self):
        return self.company_name
    
    def save(self):
        super().save()
        img = Image.open(self.service_picture.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.service_picture.path)


   

		


class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100,default=' ')
    product_desc = models.CharField(max_length=100,default=' ')
    product_price = models.IntegerField()
    product_distributer = models.ForeignKey(ServiceProvider, on_delete = models.CASCADE)
    product_image= models.ImageField(default='default.jpeg', upload_to='product_pics',null=True, blank=True)

    def __str__(self):
        return self.product_name 


    def get_absolute_url(self):
        return reverse('Product_view',kwargs={'id':self.id})

    
    def save(self):
        super().save()
        img = Image.open(self.product_image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.product_image.path)

