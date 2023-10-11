from django.urls import path, include
from .views import StoreResponse

urlpatterns = [
    path("", StoreResponse.as_view())
]
