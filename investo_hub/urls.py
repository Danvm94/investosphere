from django.urls import path

from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('wallet/', views.wallet_view, name='wallet'),
]
