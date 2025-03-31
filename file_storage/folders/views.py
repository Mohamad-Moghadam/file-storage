from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse


def new_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)

        os.makedirs(folder_path)

        return HttpResponse(f"folder was created. ")