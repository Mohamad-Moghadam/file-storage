from django.urls import path
from files.views import new_file, ls_files, rm_file


urlpatterns = [
    path('new-file/<str:destination_folder>', new_file),
    path('ls/<str:folder>', ls_files),
    path('rm/<str:folder>/<str:file>', rm_file),
]
