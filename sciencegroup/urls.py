from django.contrib import admin
from django.urls import path
from sciencegroup.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cs/',cs,name='cs'),
    path('maths/',maths,name='maths'),
    ]