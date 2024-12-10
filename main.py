import openai

# Configurar a chave de API
openai.api_key = "sua-chave-api-aqui"

def chat_with_gpt(prompt):
    """Função para interagir com o modelo ChatGPT."""
    try:
        # Fazer a chamada à API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ou "gpt-4" para modelos mais avançados
            messages=[
                {"role": "system", "content": "Você é um assistente amigável e útil."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extrair a resposta
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro: {str(e)}"

# Loop de interação com o usuário
print("Bem-vindo ao ChatGPT! Digite 'sair' para encerrar.")
while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("Encerrando o chat. Até mais!")
        break
    resposta = chat_with_gpt(entrada)
    print(f"ChatGPT: {resposta}")
