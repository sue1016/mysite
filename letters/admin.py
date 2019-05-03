from django.contrib import admin

from .models import Author,Letter,Todo

admin.site.register(Author)
admin.site.register(Letter)
admin.site.register(Todo)