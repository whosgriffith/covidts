# src/users/admin.py
# Django imports
from django.contrib import admin
# Local imports
from .models import Patient

admin.site.register(Patient)