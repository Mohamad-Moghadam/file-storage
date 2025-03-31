from django.urls import path
from folders.views import new_folder

urlpatterns = [
    path('new-folder', new_folder),
]
