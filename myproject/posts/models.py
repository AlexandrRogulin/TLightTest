from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(db_index=True, max_length=32, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    website = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    street = models.CharField(max_length=225)
    suite = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    zipcode = models.CharField(max_length=125)


class Geolocation(models.Model):
    geo = models.OneToOneField(Address, max_length=50, on_delete=models.CASCADE)
    lat = models.CharField(max_length=125)
    ing =models.CharField(max_length=125)


class Company(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    catchPhrase = models.CharField(max_length=125)
    bs = models.CharField(max_length=125)


class Post(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
