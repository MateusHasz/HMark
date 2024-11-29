from PIL import Image

try:
    # Upload the images
    imagem_fundo = Image.open("entrada.png")  # Replace with the name of your background image
    imagem_marca_dagua = Image.open("marca.png")  # The image that will be used as a watermark

    # Adjust the watermark size (optional)
    largura_fundo, altura_fundo = imagem_fundo.size
    largura_marca, altura_marca = imagem_marca_dagua.size

    # Adjusts the watermark to 50% of the background image size
    nova_largura = int(largura_fundo * 0.5)
    nova_altura = int(altura_fundo * 0.5)
    imagem_marca_dagua = imagem_marca_dagua.resize((nova_largura, nova_altura))

    # Position where the watermark will be placed
    posicao = (largura_fundo - nova_largura - 10, altura_fundo - nova_altura - 10)  # Position in the lower right corner

    # Watermark the background image
    imagem_fundo.paste(imagem_marca_dagua, posicao, imagem_marca_dagua.convert("RGBA"))  # Use "RGBA" to preserve transparency

    # Save the final image
    imagem_fundo.save("saida.jpg")

    # Display the final image (optional)
    imagem_fundo.show()

    # View Success Message
    print("Watermark added successfully! Image has been saved as 'saida.jpg'.")

except Exception as e:
    print(f"An error has occurred: {e}")
