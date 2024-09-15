from django.urls import path
from.import views


urlpatterns=[
    path('xyz/',views.display),
    path('first/',views.readData),
]