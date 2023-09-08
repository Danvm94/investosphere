from django.urls import path

from . import views

urlpatterns = [
    path('chart/', views.chart_view, name='chart'),
    path('chart_load/', views.chart_load, name='chart_load'),
    path('wallet/', views.wallet_view, name='wallet'),
    path('crypto/', views.crypto_view, name='crypto'),
    path('get_price/', views.get_price_view, name='get_price'),
]
