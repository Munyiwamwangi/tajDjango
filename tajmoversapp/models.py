from django.db import models

# Create your models here.
class Usermails(models.Model):
    name = models.CharField(max_length=30)
    subject= models.CharField (null=False,max_length=40, help_text='Current Location and Destination')
    message =  models.TextField(help_text='Tell the number of rooms and type of furniture')
    from_email = models.EmailField(null=False, help_text='Your email')
    destinations = models.CharField(null=True, max_length=20)

    class Meta:
        ordering = ('-id',)
                                       
    def __str__(self):
        return f'{self.message} from_email'
