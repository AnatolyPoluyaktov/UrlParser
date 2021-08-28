from django.urls import path
from .views import *
urlpatterns = [
    path("results/", GetResults.as_view(), name="results"),
    path("scan/",ScanUrl.as_view(), name="Scan")
]

