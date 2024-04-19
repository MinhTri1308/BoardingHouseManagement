from django.urls import path
from . import views
urlpatterns = [
    path('', views.video_feed_view, name='list_file_image'),
    # path('model-building/', views.run_python_file, name='model-building'),
    # path('detect-faces/', views.detect_faces, name='detect_faces'),
]