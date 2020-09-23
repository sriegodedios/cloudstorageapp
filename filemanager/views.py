from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import FileUpload
from django.http import HttpResponseRedirect, HttpResponse
from .models import File


def upload_file(request):
    if request.method == "POST":
        
         form = FileUpload(request.POST, request.FILES)
         files = request.FILES.getlist('file')
         print(files)
         if form.is_valid():
             for f in files:
                 file_instance = File(file=f)
                 file_instance.save()
             return HttpResponse('SUCCESS')
        
    else:
        form = FileUpload()
        return render(request, 'filemanager/uploadfile.html', {'form': form})


def upload_file2(request):
     return render(request, 'filemanager/reactupload.html')