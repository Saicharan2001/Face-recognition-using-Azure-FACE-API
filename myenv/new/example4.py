# import os
# import io
# import json
# from azure.cognitiveservices.vision.face import FaceClient
# from msrest.authentication import CognitiveServicesCredentials
# import requests
# from PIL import Image, ImageDraw, ImageFont

# """
# Example 4. Detect if a face shows up in other photos/images
# """
# # credential = json.load(open('AzureCloudKeys.json'))
# # API_KEY = credential['API_KEY']
# # ENDPOINT = credential['ENDPOINT']

# API_KEY = '43da9596256d453ba49cf10da81141b9'
# ENDPOINT = 'https://face-detecter.cognitiveaservices.azure.com/'
# face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
# response_detected_faces = face_client.face.detect_with_stream(
#     # image=open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\group.jpg", 'rb'),
#     image=open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Classroom_1.jpg", 'rb'),
#     detection_model='detection_03',
#     recognition_model='recognition_04',  
# )
# face_ids = [face.face_id for face in response_detected_faces]

# # img_source = open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Prabhas.jpg", 'rb')
# img_source = open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Abhishek.jpeg", 'rb')
# response_face_source = face_client.face.detect_with_stream(
#     image=img_source,
#     detection_model='detection_03',
#     recognition_model='recognition_04'    
# )
# face_id_source = response_face_source[0].face_id

# matched_faces = face_client.face.find_similar(
#     face_id=face_id_source,
#     face_ids=face_ids
# )

# # img = Image.open(open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\group.jpg", 'rb'))
# img = Image.open(open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Classroom_1.jpg", 'rb'))
# draw = ImageDraw.Draw(img)
# # font = ImageFont.truetype(r'C:\Windows\Fonts\OpenSans-Bold.ttf', 25)

# for matched_face in matched_faces:
#     for face in response_detected_faces:
#         if face.face_id == matched_face.face_id:
#             rect = face.face_rectangle
#             left = rect.left
#             top = rect.top
#             right = rect.width + left
#             bottom = rect.height + top
#             draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
# img.show()
import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont
"""
Example 4. Detect if a face shows up in other photos/images
"""
# credential = json.load(open('AzureCloudKeys.json'))
# API_KEY = credential['API_KEY']
# ENDPOINT = credential['ENDPOINT']

API_KEY = 'b34ca84b77474db1bc306c9acb6e5420'
ENDPOINT = 'https://face-detecter.cognitiveservices.azure.com/'
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
response_detected_faces = face_client.face.detect_with_stream(
    # image=open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\group.jpg", 'rb'),
    image=open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Classroom_1.jpg", 'rb'),
    detection_model='detection_03',
    recognition_model='recognition_04',  
)
face_ids = [face.face_id for face in response_detected_faces]
images = [r'C:\Users\saich\Desktop\DIP - Project\myenv\new\Abhishek.jpeg',r'C:\Users\saich\Desktop\DIP - Project\myenv\new\Akash.jpg']
names = ['Abhishek','Akash']
for i in range(len(images)):
    # img_source = open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Prabhas.jpg", 'rb')
    img_source = open(images[i], 'rb')
    response_face_source = face_client.face.detect_with_stream(
        image=img_source,
        detection_model='detection_03',
        recognition_model='recognition_04'    
    )
    face_id_source = response_face_source[0].face_id

    matched_faces = face_client.face.find_similar(
        face_id=face_id_source,
        face_ids=face_ids
    )

    # img = Image.open(open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\group.jpg", 'rb'))
    img = Image.open(open(r"C:\Users\saich\Desktop\DIP - Project\myenv\new\Classroom_1.jpg", 'rb'))
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(r'C:\Windows\Fonts\OpenSans-Bold.ttf', 25)

    for matched_face in matched_faces:
        for face in response_detected_faces:
            if face.face_id == matched_face.face_id:
                rect = face.face_rectangle
                left = rect.left
                top = rect.top
                right = rect.width + left
                bottom = rect.height + top
                draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
                print(names[i])
img.show()