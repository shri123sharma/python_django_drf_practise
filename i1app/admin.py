from django.contrib import admin
from i1app.models import Person, Musician, Customer, Album
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Person, PersonAdmin)


class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'instrument']


admin.site.register(Musician, MusicianAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'release_date', 'num_star']


admin.site.register(Album, AlbumAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size']


admin.site.register(Customer, CustomerAdmin)
