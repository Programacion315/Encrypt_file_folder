import os
import base64
# Walk through folder and encrypt the images inside

path_folder = ''
file = os.listdir(path_folder)
# print(file)
data = ''

for idx, i in enumerate(file):
   temporary_path_folder = '{}\\{}'.format(path_folder,file[idx])
   img = None

   with open(temporary_path_folder, 'rb') as binary_file:
      binary_file_data = binary_file.read()
      base64_encoded_data = base64.b64encode(binary_file_data)
      base64_message = base64_encoded_data.decode('utf-8')
      data = data + base64_message + '_'

data_full = ' '.join(format(ord(x), 'b') for x in data).replace(' ','')
# print(data_full)
# print('Size {}'.format(len(data_full)))

# Split string every 4 character
n = 3
data_reduce = [data_full[i:i+n] for i in range(0, len(data_full), n)]

data_reduce_number = ""
for i in data_reduce:
   if i == '111':
      data_reduce_number = data_reduce_number + '1'
   elif i == '110':
      data_reduce_number = data_reduce_number + '2'
   elif i == '101':
      data_reduce_number = data_reduce_number + '3'
   elif i == '100':
      data_reduce_number = data_reduce_number + '4'
   elif i == '011':
      data_reduce_number = data_reduce_number + '5'
   elif i == '010':
      data_reduce_number = data_reduce_number + '6'
   elif i == '001':
      data_reduce_number = data_reduce_number + '7'
   else:
      data_reduce_number = data_reduce_number + '8'

print(data_reduce_number)
print('Tamanio data full')
print(len(data_full))
print('tamanio data reduce')
print(len(data_reduce_number))
print('Convert to number to bynary?? Maybe!')

# Create a meth

# Data split
files_datas = data.split('_')
files_datas.pop()

# Open data
# for idx, i in enumerate(files_datas):
#    base64_img_bytes = i.encode('utf-8')
#    with open(str(idx) + '.png', 'wb') as file_to_save:
#       decoded_image_data = base64.decodebytes(base64_img_bytes)
#       file_to_save.write(decoded_image_data)


# Thinking...
# Combination 256... 1 byte
# Combination 16... 4 bits
# Combination 8... 3 bits

