from django.urls import path
from files.views import new_file, ls_files


urlpatterns = [
    path('new-file/<str:destination_folder>', new_file),
    path('ls_files/<str:folder>', ls_files),
]
