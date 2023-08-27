from django.urls import path

from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('wallet/', views.wallet_view, name='wallet'),
    path('crypto/', views.crypto_view, name='crypto'),
    path('get_price/', views.get_price_view, name='get_price'),
]
