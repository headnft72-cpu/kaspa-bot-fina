import tweepy, os, random, time

def postar():
    try:
        client = tweepy.Client(
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_SECRET')
        )

        # 📝 POSTS LONGOS (500-700 caracteres) - 90% Inglês
        # Agora com links didáticos em vez de números!
        posts_normais = [
            "Kaspa is the fastest and most scalable open-source, decentralized, and fully layer-1 PoW network in the world. Its blockDAG architecture allows for 1 block per second, providing the speed needed for global transactions without sacrificing security. This is the natural evolution of Satoshi's vision. \n\nExplore the tech: https://kaspa.org #KAS #Kaspa #BlockDAG",
            
            "The GHOSTDAG protocol used by Kaspa allows blocks created in parallel to coexist and be ordered in consensus. This means no energy is wasted on orphaned blocks, making it one of the most efficient Proof-of-Work networks ever built. A true masterpiece of engineering. \n\nRead the Whitepaper: https://kaspa.org/resources/ #KAS #Crypto",
            
            "Scalability in Kaspa is rooted in its ability to process multiple blocks simultaneously. Unlike traditional PoW blockchains that suffer from high orphan rates, Kaspa's DAG structure ensures every block contributes to security. This creates a massive throughput for global demand. \n\nLearn more: https://kaspa.org #KAS #Technology",
            
            "Kaspa's sub-second block times are a game-changer for merchant adoption. Waiting minutes for a confirmation is not practical for retail; Kaspa provides near-instant visual confirmation with full settlement shortly after. It's digital cash as it was meant to be. \n\nWebsite: https://kaspa.org #Fintech #KAS",
            
            "A segurança da Kaspa é herdada diretamente dos princípios de Satoshi, adaptada para a era moderna. O protocolo GHOSTDAG permite que a rede seja imune a ataques que paralisariam blockchains comuns. É o equilíbrio perfeito entre robustez e agilidade. \n\nSaiba mais em: https://kaspa.org #KaspaBrasil #KAS",
            
            "Kaspa represents the next step in decentralization. With a fair launch, no pre-mine, and no ICO, it mirrors the organic growth of early Bitcoin. It is a community-driven project focusing on solving the trilemma through innovation, not centralization. \n\nOfficial site: https://kaspa.org #Decentralization #KAS",
            
            "The transition to Rust and the goal of 10 to 100 blocks per second will make Kaspa the fastest PoW network in existence. This isn't just theory; it's being built now. The efficiency of kHeavyHash ensures high security with sustainable energy use. \n\nFollow the progress: https://kaspa.org #KAS #Layer1",
            
            "Every second counts in the digital economy. Kaspa's ability to handle high block rates without compromising the decentralization found in Proof-of-Work makes it a unique asset in the crypto space. It is designed for speed, security, and scalability. \n\nDocs: https://wiki.kaspa.org #BlockDAG #KAS"
        ]

        # 🧵 THREADS (6 PARTES)
        threads = [
            [
                "1/6 Kaspa is the world's first blockDAG, enabling parallel blocks and instant transaction confirmation. Built on a robust PoW engine with 1-second block intervals. \n\nDetails: https://kaspa.org",
                "2/6 Traditional blockchains orphan parallel blocks. GHOSTDAG allows them to coexist and orders them in consensus, solving the scalability-security tradeoff safely.",
                "3/6 Efficiency: Kaspa’s kHeavyHash algorithm ensures the network remains secure while being more energy-efficient than older PoW generations. No pre-mine, no ICO.",
                "4/6 Confirmation times: While Bitcoin takes minutes, Kaspa takes seconds. It’s designed for everyday transactions, fulfilling the original peer-to-peer cash vision.",
                "5/6 The move to Rust and 10+ blocks per second will set a new global standard. Kaspa is a foundational layer for scalable and secure PoW infrastructure. #KAS",
                "6/6 Join the evolution of the BlockDAG. Kaspa represents the next step in decentralization. Secure, fast, and community-driven. \n\
