
import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def generate_embeddings(consultants: list, model_name: str) -> pd.DataFrame:
    model = SentenceTransformer(model_name)
    texts = [c['desc_short'] for c in consultants]
    consultant_ids = [c['consultant_id'] for c in consultants]

    print(f"🔍 Gerando embeddings com o modelo: {model_name}...")
    embeddings = model.encode(texts, show_progress_bar=True)

    df = pd.DataFrame({
        'consultant_id': consultant_ids,
        'embedding': list(embeddings)
    })
    return df

def save_embeddings(df: pd.DataFrame, path: str):
    df.to_parquet(path, index=False)
