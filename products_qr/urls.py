from django.urls import path
from .views import home
app_name = 'products_qr'
urlpatterns = [
    path('', home, name='home')
]
