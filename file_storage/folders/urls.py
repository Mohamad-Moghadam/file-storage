from django.urls import path
from folders.views import new_folder, ls_folders, rm_folder

urlpatterns = [
    path('new-folder', new_folder),
    path('ls', ls_folders),
    path('rm/<str:folder>', rm_folder),
]
