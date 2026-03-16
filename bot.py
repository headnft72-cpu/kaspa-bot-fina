import tweepy, os, random, time

def postar():
    try:
        client = tweepy.Client(
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_SECRET')
        )

        # COLOQUE SEUS TEXTOS DOS PDFs ABAIXO (ENTRE AS ASPAS TRIPLAS)
        postagens = [
            """A tecnologia GHOSTDAG da Kaspa permite que os blocos coexistam.
Isso resolve o problema da mineração e da escalabilidade.

Pontos principais:
• 1 bloco por segundo (rumo a 10/s)
• Segurança Proof-of-Work real
• Descentralização total.

#Kaspa #KAS #BlockDAG""",

            """O diferencial da Kaspa está no tempo de confirmação.
Enquanto o Bitcoin leva 10 minutos, a Kaspa entrega em segundos.

A arquitetura BlockDAG permite que a rede processe múltiplos blocos 
ao mesmo tempo, sem criar 'órfãos'. 🚀"""
        ]
        
        conteudo = random.choice(postagens)
        
        # O ID abaixo garante que o Twitter não ache que o post é repetido
        texto_final = f"{conteudo}\n\n[ID: {int(time.time())}]"
        
        client.create_tweet(text=texto_final)
        print("✅ Post enviado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no terminal: {e}")

if __name__ == "__main__":
    postar()
