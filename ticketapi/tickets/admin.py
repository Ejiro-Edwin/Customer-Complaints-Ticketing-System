from django.contrib import admin
from .models import Ticket, Category, User
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(User)