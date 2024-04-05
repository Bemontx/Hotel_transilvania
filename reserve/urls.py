from django.urls import path
from .views import HomeView, ServiciosView, ReservasView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Home/',HomeView.as_view(), name='home'),
    path('Servicios-Hotel/', ServiciosView.as_view(), name='servicios'),
    path('Reservas/',ReservasView.as_view(),name='reservas')
]
