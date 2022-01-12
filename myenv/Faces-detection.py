import os
import io
import json
import sys
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
# image_url = 'https://p1.piqsels.com/preview/843/292/867/children-students-school-classroom-india-abhaneri.jpg'
image_url='https://lh3.googleusercontent.com/eEamOSgI8Ocvtyy2FTxbjfvbtJgUAFYYxH_7iP1mZke2HVFwC6iSknS2CVPxVM3dbxuaCnz410WMRDHkrr7TSAkkvVkH_L--kzsupf7vXdie_T-OPhowWWb6CzFPsm9eIixmywB7XtEsrpk6Txd_8nKkYFING6oED61LCW3jYWbVFbZMO7VxpbAc88No1DC1dwSPMswXWYaE-mPllcjQikgUMuKLDG7glAAUTQII-cGYX-LNezZUHi4Oylw5XZKYKwS_vLIDsL4CoAsbU9z-194ogzC1dePN7e9zss96MSDbf4HnWYQ4iZgt6-R_9bZ4dNeOgF3MDhNVZ6IIBDwrBpZvPJJyrJrJNnCxys6LI0V_sfmPaKNHPSLBlOnVXGp9z5Ln7u3WrYAqHiHtdcTh5UqkSslWdjfhA4hTDU6exhFuTejsO40MxYTcgERO5wGY-dkXYRuZlTU40lsyih3la5g887EtOgamZrCOlzGSKxoo5k2cYjPf3qCLD3Vr_QXgnBc3ZcWucx11qc6wrXrIQGXRvJ3sgPxWJERkYTPQqGqJtzJqaCmwDARSMXkAuVmu6sYfhSHnIAKN6pmoJi4hjumfZTSQMKZLse_0b9_SZA9X4bG6pcmzlWxIJ-Uxff84FLXFEgKCFY1eH87NLQ9xKNxcOIFqYA62aky-j3rvnEi9BlA6mMtCYx3KFwId9gntZM00jtdWSKiGkcxAJyQnjVdl=w1208-h903-no?authuser=0'
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