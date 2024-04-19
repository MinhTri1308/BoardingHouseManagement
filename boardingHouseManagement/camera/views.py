from django.shortcuts import render
import subprocess
# Create your views here.
# def create_camera(request):
#     return render(request, 'cameras/list_file_image.html')

# def face_detection_view(request):
#     return render(request, 'cameras/list_file_image.html')

# def face_detection_view(request):
#     subprocess.Popen(['python', 'E:\\Workspace\\BoardingHouseManagement\\boardingHouseManagement\\camera\\model-building.py'])
#     return render(request, 'cameras/list_file_image.html')

def face_detection_view(request):
    if request.method == 'POST':
        # Xử lý sự kiện khi nhấn vào nút "Bắt đầu nhận diện"
        subprocess.Popen(['python', 'E:\\Workspace\\BoardingHouseManagement\\boardingHouseManagement\\camera\\formadd.py'])
        return render(request, 'cameras/list_file_image.html')  # Hoặc chuyển hướng đến một trang khác nếu cần

    return render(request, 'cameras/list_file_image.html')


from django.http import JsonResponse
import cv2
from keras import models
import numpy as np

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
#
# def detect_faces(request, models = None):
#     if request.method == 'POST':
#         lstResult = ['Minh Tri', 'Nhu Luk', 'Thanh Phat', 'Trong Phu']
#
#         face_detector = cv2.CascadeClassifier('E:\\Workspace\\BoardingHouseManagement\\boardingHouseManagement\\camera\\haarcascades\\haarcascade_frontalface_default.xml')
#
#         models = models.load_model('camera/model_friend10.h5')
#         cap = cv2.VideoCapture(0)
#         while True:
#             OK, frame = cap.read()
#             # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = face_detector.detectMultiScale(frame, 1.1, 5)
#             for (x, y, w, h) in faces:
#                 roi = cv2.resize(frame[y: y + h, x: x + w], (128, 128))
#                 result = np.argmax(models.predict(roi.reshape((-1, 128, 128, 3))))
#                 print(models.predict(roi.reshape((-1, 128, 128, 3))))
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # kẻ khung
#                 cv2.putText(frame, lstResult[result], (x + 15, y - 15), cv2.FONT_ITALIC, 0.8, (255, 255, 255), 2)
#                 # ghi text lên màn hình
#             cv2.imshow('FRAME', frame)
#             if cv2.waitKey(1) & 0xff == ord('q'):
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#         subprocess.Popen(['python', 'E:\\Workspace\\BoardingHouseManagement\\boardingHouseManagement\\camera\\formadd.py'])
#         return render(request, 'cameras/list_file_image.html')  # Hoặc chuyển hướng đến một trang khác nếu cần
#
#     return render(request, 'cameras/list_file_image.html')

import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from keras.models import load_model  # Import thư viện models từ keras

lstResult = ['Minh Tri', 'Nhu Luk', 'Thanh Phat', 'Trong Phu']
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
models = load_model('camera/model_friend10.h5')  # Sử dụng load_model từ keras để tải model

@gzip.gzip_page
def video_feed(request, models=None):  # Thêm tham số models vào hàm video_feed
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_detector.detectMultiScale(frame, 1.1, 5)
        for (x, y, w, h) in faces:
            roi = cv2.resize(frame[y: y + h, x: x + w], (128, 128))
            result = models.predict(roi.reshape((-1, 128, 128, 3)))  # Thêm .reshape để phù hợp với kích thước đầu vào của model
            print(result)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, lstResult[result.argmax()], (x + 15, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

def video_feed_view(request):
    generator = video_feed(request, models)
    response = StreamingHttpResponse(generator, content_type='multipart/x-mixed-replace; boundary=frame')

    if not generator:
        return StreamingHttpResponse(b'')  # Trả về một StreamingHttpResponse rỗng nếu generator không có giá trị

    return response