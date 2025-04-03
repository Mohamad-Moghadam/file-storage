from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from folders.models import Folder
import os
from files.models import File
from django.http import HttpResponse
from django.conf import settings
import shutil


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


def ls_files(request, folder: str):
    the_folder = get_object_or_404(Folder, name= folder)
    files_in_folder = the_folder.the_folder_that_contains_the_file.all()

    context = {
        'folder': the_folder,
        'files': files_in_folder
    }

    return render(request, "all_files/all_files.html", context)


def rm_file(request, folder: str, file: str):
    the_folder= get_object_or_404(Folder, name= folder)

    the_file = get_object_or_404(the_folder.the_folder_that_contains_the_file, name=file)
    file_name = the_file.name

    the_file.delete()

    folder_path= os.path.join(settings.MEDIA_ROOT, the_folder.name)

    file_path = os.path.join(settings.MEDIA_ROOT, folder, file_name)

    os.remove(file_path)

    return HttpResponse(f"{file_name} is removed. ")