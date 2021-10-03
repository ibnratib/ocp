from django.db import models

# Create your models here.
class contact(models.Model):
	Name=models.CharField(max_length=30)
	Subject = models.CharField(max_length=30)
	Email = models.EmailField(max_length=40)
	Message = models.TextField()
	send_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
			return "%s" % (self.Email)