from django.contrib import admin
from django.urls import path
from App_family.views import create_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new-person/', create_person, name="create_person"),
]
