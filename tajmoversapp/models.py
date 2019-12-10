from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name =models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)

class Usermails(models.Model):
    name = models.CharField(max_length=30)
    subject= models.CharField (null=False,max_length=40, help_text='Moving from where to where?')
    message =  models.TextField(help_text='Tell the number of rooms and type of furniture, <br> may be 3 beds, one 2 seater sofa, e.t.c')
    from_email = models.EmailField(null=False, help_text='Your email')
    destinations = models.CharField(null=True, max_length=20)

    class Meta:
        ordering = ('-id',)
                                       
    def __str__(self):
        return f'{self.message} from_email'
