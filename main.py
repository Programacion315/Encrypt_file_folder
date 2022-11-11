import os
import base64

# Walk through folder and encrypt the images inside

path_folder = ''

file = os.listdir(path_folder)

print(file)

# print

img = None

with open('01.png', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    print(base64_message)
    img = base64_message

base64_img = img

base64_img_bytes = base64_img.encode('utf-8')
with open('encode.png', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)