import tweepy, os, random, time

def postar():
    try:
        client = tweepy.Client(
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_SECRET')
        )

        # POSTS LONGOS (500-700 CARACTERES) - 90% INGLÊS
        posts_normais = [
            """Kaspa's GHOSTDAG architecture is a fundamental shift in blockchain technology. By allowing blocks to coexist in parallel, it achieves a block rate that linear chains simply cannot match. This means 1 block per second today, with the potential for much more. The security remains pure Proof-of-Work, ensuring decentralization isn't sacrificed for speed. It's the ultimate solution to the trilemma, providing a robust environment for real-world digital silver use cases and mass adoption. [ID: {id}]""",
            """The scalability of Kaspa is rooted in its ability to process multiple blocks simultaneously. Unlike traditional PoW blockchains that suffer from high orphan rates when speed is increased, Kaspa's DAG structure ensures every block contributes to network security. This creates a massive throughput that can support global demand while remaining decentralized. It is a technological masterpiece in the crypto space, fulfilling the original vision of peer-to-peer electronic cash. [ID: {id}]""",
            """The sub-second block times of Kaspa are a game-changer for merchant adoption. Waiting 10 minutes for a Bitcoin confirmation or even minutes for other chains is not practical for retail. Kaspa provides near-instant visual confirmation, with full settlement following shortly after. It's the only PoW chain that actually functions like cash in a digital environment, combining the robustness of gold with the speed of light. #Kaspa #KAS #Crypto [ID: {id}]""",
            """A segurança da Kaspa é herdada diretamente dos princípios de Satoshi, mas adaptada para a era moderna. O protocolo GHOSTDAG permite que a rede seja imune a ataques que paralisariam blockchains comuns. É o equilíbrio perfeito entre a robustez do ouro digital e a agilidade necessária para o comércio global. Kaspa é, sem dúvida, a evolução do consenso Nakamoto e o futuro das transações descentralizadas rápidas. [ID: {id}]"""
        ]

        # THREADS (6 PARTES - 240-247 CARACTERES CADA)
        threads = [
            [
                "1/6 Kaspa is the world's first blockDAG, a digital ledger enabling parallel blocks and instant transaction confirmation. Built on a robust proof-of-work engine with rapid single-second block intervals for maximum speed.",
                "2/6 Traditional blockchains orphan parallel blocks. GHOSTDAG allows them to coexist and orders them in consensus. This architecture solves the scalability-security tradeoff, allowing high block rates safely and securely.",
                "3/6 Efficiency is key: Kaspa’s kHeavyHash algorithm ensures the network remains secure while being energy-efficient compared to older PoW generations. It is a fair launch project with no pre-mine or private sales.",
                "4/6 Confirmation times: While Bitcoin takes minutes, Kaspa takes seconds. It’s designed to be used for everyday transactions, fulfilling the original vision of a truly decentralized peer-to-peer electronic cash system.",
                "5/6 The move to Rust and 10 blocks per second will set a new standard. Kaspa is not just a coin; it's a foundational layer for the future of decentralized finance on a scalable and secure PoW infrastructure today.",
                "6/6 Join the evolution of the BlockDAG. Kaspa represents the next step in decentralization. Secure, fast, and community-driven. The future of mining and transactions is here with #Kaspa #KAS #BlockDAG #Crypto"
            ]
        ]

        agora = time.gmtime()
        # Se a hora for 0, 8 ou 16 (UTC), envia Thread. Senão, post normal.
        if agora.tm_hour in [0, 8, 16] and agora.tm_min < 20:
            print("🕒 Hora da Thread (8h em 8h)!")
            fio = random.choice(threads)
            ultimo_id = None
            for parte in fio:
                response = client.create_tweet(text=parte, in_reply_to_tweet_id=ultimo_id)
                ultimo_id = response.data['id']
                time.sleep(2)
            print("✅ Thread enviada!")
        else:
            print("🕒 Hora do Post normal (Frequência de 80 min)!")
            texto = random.choice(posts_normais).format(id=int(time.time()))
            client.create_tweet(text=texto)
            print("✅ Post enviado!")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    postar()
