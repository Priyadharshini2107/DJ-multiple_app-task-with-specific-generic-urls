from django.contrib import admin
from django.urls import path
from artsgroup.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BBA/',BBA,name='BBA'),
    path('BCOM/',BCOM,name='BCOM'),
    ]