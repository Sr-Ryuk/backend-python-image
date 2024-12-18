import requests

# URL do backend Flask (mude se necessário)
url = "http://127.0.0.1:5000/process-image"

# Envia a imagem para o servidor e salva a resposta
try:
    with open("input.png", "rb") as img_file:  # Abre a imagem de entrada
        response = requests.post(url, files={"image": img_file})

    if response.status_code == 200:
        # Salva a imagem recebida do servidor
        with open("output.png", "wb") as f:
            f.write(response.content)
        print("Imagem processada salva como 'output.png'")
    else:
        print("Erro ao processar a imagem:", response.json())

except Exception as e:
    print("Ocorreu um erro:", str(e))
