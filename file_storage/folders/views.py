from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from folders.models import Folder
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def new_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)

        os.makedirs(folder_path)

        Folder.objects.create(
            name = folder_name.get('folder_name')
        )

        return HttpResponse(f"folder was created. ")