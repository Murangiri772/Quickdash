
from django.contrib import admin
from django.urls import path
from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),
    path('gallary/', views.gallary, name='gallary'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('product/', views.product, name='product'),
    path('services/', views.services, name='services'),

]
