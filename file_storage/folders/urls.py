from django.urls import path
from folders.views import new_folder, ls_folders

urlpatterns = [
    path('new-folder', new_folder),
    path('ls', ls_folders),
]
