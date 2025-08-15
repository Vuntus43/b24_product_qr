from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('p/<uuid:token>/', views.public_product_page, name='public_product_page'),
]
