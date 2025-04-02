from django.shortcuts import render, get_object_or_404
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from folders.models import Folder
from django.views.decorators.csrf import csrf_exempt
import shutil


@csrf_exempt
def new_folder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')

        folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
        

        os.makedirs(folder_path)

        Folder.objects.create(
            name = folder_name
        )

        return HttpResponse(f"folder was created. ")


def ls_folders(request):
    context = {
        'folders': Folder.objects.all()
    }

    return render(request, "all_folders/all_folders.html", context)


def rm_folder(request, folder: str):
    the_folder = get_object_or_404(Folder, name= folder)

    the_folder.delete()
    folder_name = the_folder.name

    folder_path = os.path(settings.MEDIA_ROOT, folder_name)

    shutil.rmtree(folder_path)

    return HttpResponse(f"{the_folder.name} deleted. ")