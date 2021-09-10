from django.contrib import admin
from django.contrib.auth import models
# from django.contrib.auth.base_user import AbstractBaseUser
from .models import  Company, CustomUser, Geolocation, Post, Address
from django.contrib.auth.models import AbstractBaseUser



class CustomAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'website')
    search_fields = ('name', 'username', 'email', 'phone', 'website')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'suite', 'city', 'zipcode')
    search_fields = ('street', 'suite', 'city', 'zipcode')


class GeolocationAdmin(admin.ModelAdmin):
    list_display = ('geo', 'lat', 'ing')
    search_fields = ('geo', 'lat', 'ing')


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'author', 'title', 'body') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('body', 'title', 'author')
    empty_value_display = '-пусто-'


# admin.site.register(User, UserAdmin)
# admin.site.register(Address, AddressAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Company)
admin.site.register(Geolocation, GeolocationAdmin)