from django.contrib import admin

from .models.citizen import Citizen
from .models.home import Home, Livestock

admin.site.register(Citizen)
admin.site.register(Home)
admin.site.register(Livestock)
