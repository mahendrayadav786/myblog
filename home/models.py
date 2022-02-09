from django.db import models
# Create your models here.


class Contact(models.Model):
     sn = models.AutoField(primary_key= True)
     name = models.CharField(max_length=500)
     phone = models.CharField(max_length=15)
     email = models.CharField(max_length=100)
     textarea = models.TextField()
     timestamp = models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return self.name