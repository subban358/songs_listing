from django.contrib import admin
from .models import Artists, Songs, Ratings
# Register your models here.

admin.site.register(Artists)
admin.site.register(Songs)
admin.site.register(Ratings)