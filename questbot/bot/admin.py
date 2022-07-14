from django.contrib import admin

from .models import Menu, Button, Content, Slug

admin.site.register(Menu)
admin.site.register(Button)
admin.site.register(Content)
admin.site.register(Slug)