from django.urls import path
from files.views import new_file


urlpatterns = [
    path('new-file/<str:destination_folder>', new_file)
]
