from django.contrib import admin
from .models import Celebrities, Maths, Film, Literature

# Register your models here.
admin.site.register(Celebrities)
admin.site.register(Maths)
admin.site.register(Film)
admin.site.register(Literature)