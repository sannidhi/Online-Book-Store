from django.db import models


class Member(models.Model):
    Memberid = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length=20)

class Product(models.Model):
    Productid = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    isbn = models.IntegerField(max_length=20)
    price = models.FloatField()

    @models.permalink
    def get_absolute_url(self):
        return ('product_view', [str(self.id)])

	def __str__(self):
		return '%s [%s]' % (self.Productid, self.title)
