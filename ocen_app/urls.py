from django.urls import path, include
from .views import APISimulatorView

urlpatterns = [
    path("", APISimulatorView.as_view())
]
