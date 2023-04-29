import os
import base64
import sys
import time

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

   print(data_reduce)

   for i in range(len(data_reduce)):
        if data_reduce[i] == '10':
            data_reduce[i] = '2'
        elif data_reduce[i] == '01':
            data_reduce[i] = '4'
        elif data_reduce[i] == '11':
            data_reduce[i] = '6'
        elif data_reduce[i] == '00':
            data_reduce[i] = '8'

   data_str = ''.join(data_reduce)

   data_reduce = [data_str[i:i+n] for i in range(0, len(data_str), n)]

   # Se hace la validacion si el grupo es igual

   flag = None #Thelas number
   ultimo_numero = int(data_reduce[-1])

   print(data_reduce)

   if len(str(ultimo_numero)) == 1:
      flag = ultimo_numero
      data_reduce.pop()


   print(data_reduce)




   data_str = ''.join(data_reduce)

   print(int(data_str))

    #Dividiro

   data_int = int(data_str)
   print(data_int)

#    for i in range(10000, 100000):
#       if data_int % i == 0:
#         print(f"El número " + str(i))

   while len(str(data_int)) > 4:

      data_int = data_int - 1000000000000000

      print(data_int)
      time.sleep(1)

    # Find maximun dividor












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




