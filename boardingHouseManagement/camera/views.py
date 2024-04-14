from django.shortcuts import render

# Create your views here.
def create_camera(request):
    return render(request, 'cameras/list_file_image.html')