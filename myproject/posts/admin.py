from django.contrib import admin
from django.contrib.auth import models
from .models import Company, CustomUser, Geolocation, Post, Address


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
    list_display = ('id', 'author', 'title', 'body')
    search_fields = ('body', 'title', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Company)
admin.site.register(Geolocation, GeolocationAdmin)
