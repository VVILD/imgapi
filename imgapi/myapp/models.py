from django.db import models

# Create your models here.


class Foo(models.Model):
	img = models.ImageField(upload_to="myapp/foo/images", null=True, blank=True)
	body = models.CharField(max_length=10)
	