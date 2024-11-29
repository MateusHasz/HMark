# HMark
Simple python script where you automatically add a watermark to an image

Code Breakdown:
==============================================================================================================================================================================
from PIL import Image: This imports the Image module from the Pillow library. The Image module allows you to open, manipulate, and save images. It is the core tool for working with images in this script.
==============================================================================================================================================================================

try:: The try block is used to attempt executing the code inside it. If any errors occur during execution, the code inside the except block will be executed. This is a mechanism for exception handling.

==============================================================================================================================================================================
Image.open("entrada.png"): The Image.open() function is used to open an image file. Here, it loads the "entrada.png" image to be used as the background image and the "marca.png" image to be used as the watermark.
imagem_fundo and imagem_marca_dagua now contain the objects representing these images, allowing you to manipulate them (resize, paste one over the other, etc.).
==============================================================================================================================================================================
imagem_fundo.size and imagem_marca_dagua.size: The .size property of an Image object returns a tuple containing the image's dimensions in the format (width, height).
largura_fundo, altura_fundo: Stores the dimensions of the background image.
largura_marca, altura_marca: Stores the dimensions of the watermark image.
==============================================================================================================================================================================
nova_largura = int(largura_fundo * 0.5) and nova_altura = int(altura_fundo * 0.5): These lines calculate the new size for the watermark. In this case, we want the watermark to be 50% of the width and height of the background image. The calculation uses the background image size to set the watermark size.
nova_largura and nova_altura are the new dimensions for the watermark.
imagem_marca_dagua.resize((nova_largura, nova_altura)): The .resize() function resizes the watermark image to the new dimensions calculated earlier.
==============================================================================================================================================================================
posicao: The posicao variable defines where the watermark will be placed on the background image. In this case, the watermark is positioned at the bottom-right corner of the image.
largura_fundo - nova_largura - 10: Positions the watermark horizontally with a 10-pixel margin from the right edge.
altura_fundo - nova_altura - 10: Positions the watermark vertically with a 10-pixel margin from the bottom edge.
==============================================================================================================================================================================
imagem_fundo.paste(): The paste() function is used to paste one image on top of another. It takes three parameters:
The image to be pasted (the watermark image, imagem_marca_dagua).
The position where the image should be pasted (defined by the posicao variable).
The mask: The third argument imagem_marca_dagua.convert("RGBA") ensures that the transparency of the watermark is preserved when pasting it onto the background image. The conversion to "RGBA" is important because the RGBA format includes an alpha channel for transparency.
This allows the transparent watermark to be pasted on top of the background image without covering up undesired parts of the background.
==============================================================================================================================================================================
imagem_fundo.save("saida.jpg"): The save() function saves the resulting image (with the watermark) to a file. In this case, the image is saved as "saida.jpg".
You can change the file format (e.g., .png, .bmp, etc.) depending on your requirements.
==============================================================================================================================================================================
imagem_fundo.show(): The show() function displays the final image in the default image viewer on your operating system (e.g., Windows Photo Viewer or Preview on macOS). This is useful for quickly checking if the result is as expected.
==============================================================================================================================================================================
print("Marca d'água adicionada com sucesso! A imagem foi salva como 'saida.jpg'."): The print() function displays the message in the terminal or command prompt. Here, it informs that the script was successfully executed and the image was saved as "saida.jpg".
==============================================================================================================================================================================
except Exception as e:: The except block is used to catch and handle any errors that may occur in the try block. If any error happens during the process (e.g., if the images are missing or there are issues reading them), the exception is caught and an error message is displayed.
Exception: This is the generic exception class that catches any kind of error.
e: The variable e captures the error message associated with the exception that occurred.
print(f"Ocorreu um erro: {e}"): If an error occurs, this line will print the error message in the terminal, helping to diagnose what went wrong.
==============================================================================================================================================================================
Summary of Key Functions:
Image.open(): Opens an image file and loads it into an Image object.
Image.size: Returns the dimensions of an image as a tuple (width, height).
Image.resize(): Resizes the image to new dimensions specified.
Image.paste(): Pastes one image on top of another at a specific position with or without a transparency mask.
Image.save(): Saves the image to a file in the desired format.
Image.show(): Displays the image in the default system image viewer.
try and except: A structure for exception handling, which allows you to catch and handle errors that may occur during code execution.
This script not only adds a watermark to an image but also provides feedback on whether the process was successful or if an error occurred.
==============================================================================================================================================================================
