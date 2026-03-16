import tweepy, os, random, time

def postar():
    try:
        # O robô vai ler os nomes que você acabou de criar nos Secrets
        client = tweepy.Client(
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_SECRET')
        )

        # Frases baseadas na tecnologia Kaspa
        frases = [
            "Kaspa: O protocolo GHOSTDAG permite escalabilidade real sem perder segurança.",
            "Diferente do Bitcoin, Kaspa processa blocos em paralelo usando BlockDAG.",
            "A segurança do Proof of Work com a velocidade da luz: Isso é Kaspa.",
            "O algoritmo kHeavyHash torna a mineração de Kaspa eficiente e única.",
            "Kaspa (KAS) é a evolução do consenso de Nakamoto."
        ]
        
        # Escolhe uma frase e adiciona um ID de tempo para evitar o erro de post repetido
        texto = f"{random.choice(frases)} [Ref: {int(time.time())}]"
        
        client.create_tweet(text=texto)
        print("✅ Post enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao postar: {e}")

if __name__ == "__main__":
    postar()
