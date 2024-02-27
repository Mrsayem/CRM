from django.db import models

# Create your models here.
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	divison =  models.CharField(max_length=50)
	image =  models.ImageField(upload_to='images/')
	def __str__(self):
		return(f"{self.name}")