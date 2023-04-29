from PIL import Image

img = Image.open('chaos.png')

img = img.convert('RGB')

# Establecer el nivel de calidad para la compresión
quality = 1

# Guardar la imagen en formato JPEG con el nivel de calidad seleccionado
img.save('comprimida.jpg', quality=quality)