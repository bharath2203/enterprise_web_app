from django.contrib import admin

# Register your models here.


from .models import Data, User

admin.site.register(Data)
admin.site.register(User)
