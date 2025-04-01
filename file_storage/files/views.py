from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from folders.models import Folder
import os
from files.models import File
from django.http import HttpResponse
from django.conf import settings


@csrf_exempt
def new_file(request, destination_folder: str):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        folder = get_object_or_404(Folder, name= destination_folder)
        folder_path = os.path.join(settings.MEDIA_ROOT, folder.name)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as f:
                pass

        File.objects.create(
            name = file_name,
        )

        return HttpResponse(f"file created. ")
