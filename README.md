# TUTOR-TPU-
Système d'apprentissage basé sur l'IA adaptatives et les modèles cognitifs 
# Cours sur l'IA Adaptative et les Modèles Cognitifs

## Cours 1 : Introduction à l'IA Adaptative  
L'IA adaptative se réfère aux systèmes capables de modifier leur comportement en fonction de nouvelles données.  
- Exemples : Systèmes de recommandation, assistants vocaux, etc.

---

## Cours 2 : Principes des Modèles Cognitifs  
Les modèles cognitifs visent à simuler le fonctionnement de la pensée humaine.  
- Exemples : ACT-R, SOAR, réseaux de neurones symboliques.

---

## Cours 3 : Applications combinées  
- Enseignement intelligent (tuteurs intelligents)  
- Interface cerveau-machine  
- Personnalisation dans les jeux et formations

---

## Exercice Pratique 1  
Créez une fonction Python qui simule une mémoire adaptative :

```python
memoire = {}

def ajouter_ou_mettre_a_jour(cle, valeur):
    memoire[cle] = valeur
    return memoire

# Exemple d’usage
print(ajouter_ou_mettre_a_jour('cours1', 'IA adaptative'))
def tuteur_intelligent(note):
    if note >= 15:
        return 'Très bien, continue comme ça !'
    elif note >= 10:
        return 'Pas mal, mais tu peux faire mieux.'
    else:
        return 'Révise le cours et essaie encore.'

# Exemple d’usage
for note in [18, 12, 7]:
    print(note, "→", tuteur_intelligent(note))
import sqlite3
import faiss
import torch
import torch.nn as nn
import numpy as np
import subprocess
# Remove the import statement for docker
# import docker
from transformers import pipeline, AutoModel, AutoTokenizer

# 1. Stockage des données fractales
class FractalStorage:
    def __init__(self, db_path='fractal_data.db'):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS fractals (
                                id INTEGER PRIMARY KEY,
                                vector BLOB,
                                metadata TEXT)''')

    def add_fractal(self, vector: np.ndarray, metadata: dict):
        self.conn.execute("INSERT INTO fractals (vector, metadata) VALUES (?, ?)",
                          (vector.tobytes(), str(metadata)))
        self.conn.commit()

    def get_fractal(self, fractal_id: int):
        cur = self.conn.execute("SELECT vector, metadata FROM fractals WHERE id=?", (fractal_id,))
        blob, meta = cur.fetchone()
        return np.frombuffer(blob, dtype=np.float32), eval(meta)

# 2. Compression fractale avec auto-encodeur
class FractalAutoencoder(nn.Module):
    def __init__(self, input_dim=768, latent_dim=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))

# 3. Index FAISS avec compression
class FractalIndex:
    def __init__(self, dim=128):
        self.index = faiss.IndexIVFFlat(faiss.IndexFlatL2(dim), dim, 100)
        self.autoencoder = FractalAutoencoder(input_dim=768, latent_dim=dim)
        # self.autoencoder.load_state_dict(torch.load('fractal_ae.pth')) # Commented out as the file doesn't exist yet

    def add_vector(self, vector: np.ndarray):
        compressed = self._compress(vector)
        if not self.index.is_trained:
            # Assuming you have a way to collect training data for the index
            # For now, I'll add a placeholder. You'll need to replace this
            # with actual training data before using the index.
            placeholder_train_data = np.random.rand(1000, self.index.d).astype('float32')
            # Ensure training data is compressed before training the index
            compressed_train_data = self._compress_batch(placeholder_train_data)
            self.index.train(compressed_train_data)
        self.index.add(compressed)

    def _compress(self, vector: np.ndarray):
        with torch.no_grad():
            tensor = torch.from_numpy(vector.reshape(1, -1)).float()
            return self.autoencoder.encoder(tensor).numpy().astype('float32') # Ensure float32

    def _compress_batch(self, vectors: np.ndarray):
         with torch.no_grad():
            tensor = torch.from_numpy(vectors).float()
            return self.autoencoder.encoder(tensor).numpy().astype('float32') # Ensure float32


# 4. Orchestrateur multi-modèles
class HybridAIOrchestrator:
    def __init__(self):
        # Local processing with Hugging Face pipeline
        self.local_llm = pipeline('text-generation', model='gpt2', device=-1)

        # Cloud processing simulated with Hugging Face models
        # Using separate pipelines for text generation and embeddings for clarity
        self.cloud_llms = {
            'hf_text_gen': pipeline('text-generation', model='gpt2', device=-1), # Using gpt2 as a placeholder
            'hf_embeddings': pipeline('feature-extraction', model='bert-base-uncased', device=-1) # Using bert-base-uncased for embeddings
        }


    def query(self, prompt: str, use_cloud=True):
        # Local processing
        local_result = self.local_llm(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']

        if use_cloud:
            # Cloud processing
            cloud_results = {}
            try:
                # Using the Hugging Face text generation pipeline for the 'cloud' LLM
                cloud_results['hf_text_gen'] = self.cloud_llms['hf_text_gen'](
                    prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
            except Exception as e:
                print(f"Cloud error (hf_text_gen): {str(e)}")

            try:
                # Using the Hugging Face feature extraction pipeline for embeddings
                # The output format can vary, so we take the mean of the token embeddings
                embeddings_output = self.cloud_llms['hf_embeddings'](prompt)
                # The output is usually a list of lists of floats
                # We take the first element (for the first prompt) and the mean across tokens
                cloud_results['hf_embeddings'] = np.mean(embeddings_output[0], axis=0)
            except Exception as e:
                print(f"Cloud error (hf_embeddings): {str(e)}")


            # Fusion fractale des résultats
            return self._fractal_fusion(local_result, cloud_results)
        return local_result

    def _fractal_fusion(self, local, cloud):
        # Fusion by cosine similarity, adapted for Hugging Face pipeline outputs
        hf_text_gen_result = cloud.get('hf_text_gen', None)
        hf_embeddings_result = cloud.get('hf_embeddings', None)

        if hf_text_gen_result is not None and hf_embeddings_result is not None and isinstance(hf_embeddings_result, np.ndarray):
             # For demonstration, we can't directly calculate cosine similarity between text and an embedding vector.
             # A more realistic approach would involve embedding the hf_text_gen_result as well.
             # As a simplified fusion, we can combine the text results.
             return f"FUSION: Local({local[:50]}...) + Cloud(HF Text Gen: {hf_text_gen_result[:50]}...)"

        elif hf_text_gen_result is not None:
             return f"FUSION: Local({local[:50]}...) + Cloud(HF Text Gen: {hf_text_gen_result[:50]}...)"

        # If only embeddings are available or neither is available, just return local for now
        return local


# 5. Noyau fractal TPU++ simulé
class FractalKernel:
    def __init__(self, alpha=1.8, history_size=100):
        self.alpha = alpha
        self.history = np.zeros(history_size)

    def convolve(self, x):
        kernel = self._generate_fractal_kernel(len(x))
        return np.convolve(x, kernel, mode='same')

    def _generate_fractal_kernel(self, size):
        t = np.linspace(0, 1, size)
        return np.power(t + 1e-9, -self.alpha)

# 6. Générateur de code sécurisé
class CodeGenerator:
    def __init__(self):
        # self.client = docker.from_env() # Commented out as Docker setup is not guaranteed in Colab
        self.container = None
        # Use Hugging Face pipeline for code generation simulation
        self.code_gen_pipeline = pipeline('text-generation', model='gpt2', device=-1) # Using gpt2 as a placeholder

    def generate_and_run(self, task_description):
        # Génération avec modèle cloud (simulated with HF pipeline)
        prompt = f"Write Python code for: {task_description}"
        # Generate code using the HF pipeline
        generated_code = self.code_gen_pipeline(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

        # Simulate execution in a Docker container - Further simplified
        try:
            # In a real scenario, you would run 'generated_code' in a secure environment.
            # Here, we'll just print the simulated code and execution message.
            simulated_logs = f"Simulated code execution for: '{task_description}'\n--- Simulated Code ---\n{generated_code}\n--- End Simulation ---"
            return {"status": "success", "logs": simulated_logs}
        except Exception as e:
            return {"status": "error", "message": str(e)}

# 7. Workflow intégré
def main():
    # Configuration
    torch.set_num_threads(4)  # Optimisation pour CPU

    # Initialisation des composants
    storage = FractalStorage()
    orchestrator = HybridAIOrchestrator()
    kernel = FractalKernel()
    code_gen = CodeGenerator()

    # Exemple de workflow
    prompt = "Simuler une onde fractale avec convolution temporelle"

    # Requête hybride
    response = orchestrator.query(prompt)
    print(f"Réponse IA: {response}")

    # Génération et exécution de code
    code_result = code_gen.generate_and_run(prompt)
    print(f"Résultat exécution: {code_result}")

    # Simulation de convolution fractale
    signal = np.random.randn(100)
    fractal_signal = kernel.convolve(signal)
    print(f"Signal transformé: {fractal_signal[:5]}...")

if __name__ == "__main__":
    main()
