import tweepy, os, random, time

def postar():
    try:
        client = tweepy.Client(
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_SECRET')
        )

        # 📚 CONTEÚDO DOS SEUS DOCUMENTOS
        postagens = [
            """A tecnologia GHOSTDAG da Kaspa é revolucionária. 
Diferente das blockchains lineares, ela permite que blocos criados em paralelo sejam integrados à rede sem desperdício.

Isso resolve o trilema:
1. Segurança PoW 🛡️
2. Velocidade absurda ⚡
3. Descentralização real 🌍""",

            """Você sabia que a Kaspa utiliza o algoritmo kHeavyHash? 
Ele foi projetado para ser eficiente e permitir que a rede mantenha 1 bloco por segundo com segurança total. 

O futuro do dinheiro digital é agora! 🚀""",

            """Kaspa: A evolução do consenso de Nakamoto. 
Sem pré-mineração, sem vendas privadas, sem ICO. 

É um projeto de lançamento justo (fair launch) onde a comunidade vem em primeiro lugar. 💎 #KAS #Kaspa""",

            """O tempo de confirmação na rede Kaspa é quase instantâneo. 
Enquanto outras redes levam minutos, a estrutura BlockDAG permite transações rápidas para o uso no dia a dia.✨"""
        ]
        
        conteudo = random.choice(postagens)
        
        # O ID abaixo garante que o Twitter aceite o post como único
        texto_final = f"{conteudo}\n\n[ID: {int(time.time())}]"
        
        client.create_tweet(text=texto_final)
        print(f"✅ Postagem única enviada!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    postar()
