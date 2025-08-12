
import wikipedia
import os

topics = [
    "Artificial intelligence",
    "Machine learning",
    "Deep learning",
    "Neural network",
    "Natural language processing",
    "Computer vision",
    "Reinforcement learning",
    "Supervised learning",
    "Unsupervised learning",
    "Support-vector machine",
    "Decision tree",
    "Random forest",
    "Convolutional neural network",
    "Generative adversarial network"
]

save_dir = "data/raw"
os.makedirs(save_dir, exist_ok=True)

for topic in topics:
    try:
        print(f"Downloading article: {topic}")
        page = wikipedia.page(topic)
        content = page.content

        filename = topic.lower().replace(" ", "_") + ".txt"
        filepath = os.path.join(save_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved: {filepath}")

    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation error for '{topic}': options - {e.options}")
    except wikipedia.PageError:
        print(f"Page not found: {topic}")
    except Exception as e:
        print(f"Error downloading '{topic}': {e}")
