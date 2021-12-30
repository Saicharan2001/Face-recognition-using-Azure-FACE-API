import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont
"""
Example 1. Detect faces from an image (from the web)
"""

# credential = json.load(open('AzureCloudKeys.json'))
API_KEY = 'b34ca84b77474db1bc306c9acb6e5420'
ENDPOINT = 'https://face-detecter.cognitiveservices.azure.com/'

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
# image_url = 'https://earthyphotography.co.uk/wp-content/uploads/2020/04/composite-corporate-group-photos-02.jpg'
# image_url = '.Training_images\Train.jpg'
# image_url = 'https://media.istockphoto.com/photos/large-group-of-students-studying-on-a-class-in-the-classroom-picture-id1163483094'
image_url = 'https://p1.piqsels.com/preview/843/292/867/children-students-school-classroom-india-abhaneri.jpg'

image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_03',
    recognition_model='recognition_04'

)
print(response_detected_faces)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
img.show()
img.save('test.jpg')