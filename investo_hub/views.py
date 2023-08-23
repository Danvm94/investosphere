from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import os

def portfolio_view(request):
    return render(request, 'portfolio.html')