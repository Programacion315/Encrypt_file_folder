import os
import base64
import sys

count = 0
count2 = 0

def zipImage():

   global count
   global count2

   path_folder = './images'
   file = os.listdir(path_folder)

   data = ''

   for idx, i in enumerate(file):
      temporary_path_folder = os.path.join(path_folder, file[idx])
      img = None

      with open(temporary_path_folder, 'rb') as binary_file:
         binary_file_data = binary_file.read()
         base64_encoded_data = base64.b64encode(binary_file_data)
         base64_message = base64_encoded_data.decode('utf-8')
         data = data + base64_message + '_'

   data_full = ' '.join(format(ord(x), 'b') for x in data).replace(' ','')

   n = 2
   data_reduce = [data_full[i:i+n] for i in range(0, len(data_full), n)]

   while '10' in data_reduce or '01' in data_reduce:
      for i in range(len(data_reduce)):
         if data_reduce[i] == '10':
               data_reduce[i] = '1'
         elif data_reduce[i] == '01':
               data_reduce[i] = '0'

      data_str = ''.join(data_reduce)

      data_reduce = [data_str[i:i+n] for i in range(0, len(data_str), n)]
      count = count + 1

   print("Vueltas = " + str(count))


   n = 2
   data_reduce = [data_str[i:i+n] for i in range(0, len(data_str), n)]

   while '00' in data_reduce or '11' in data_reduce:
      for i in range(len(data_reduce)):
         if data_reduce[i] == '00':
               data_reduce[i] = '0'
         elif data_reduce[i] == '11':
               data_reduce[i] = '1'

      data_str = ''.join(data_reduce)

      data_reduce = [data_str[i:i+n] for i in range(0, len(data_str), n)]
      print(data_reduce)
      count2 = count2 + 2

   print('Vueltas2 = ' + str(count2))
   data_str = ''.join(data_reduce)
   print(data_str)


   print('Total de vueltas: ' + str((count + count2)))


def unzipImage(compressed_data):
    parts = compressed_data.split("_")
    message = parts[0]
    c2 = int(parts[2])

    n = 1
    messageList = [message[i:i+n] for i in range(0, len(message), n)]
    print(messageList)

    i = 0
    while i < int(parts[1]):
        for j in range(len(messageList)):
            if messageList[j] == '0':
                messageList[j] = '00'
            elif message[j] == '1':
                messageList[j] = '11'
        i = i + 1
        print(messageList)
        data_str = ''.join(messageList)
        messageList = [data_str[i:i+n] for i in range(0, len(data_str), n)]

    print(messageList)

print('Welcome!')

option = input('To compress type 1, if you want to decompress type 2: ')

if option == '1':
    zipImage()
else:
    bestt = input('Type the bestt: ')
    unzipImage(bestt)




