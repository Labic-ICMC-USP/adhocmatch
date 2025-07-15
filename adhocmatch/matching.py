
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def get_top_k_consultants(project_desc_short: str, embeddings_df: pd.DataFrame, model_name: str, top_k: int) -> pd.DataFrame:
    model = SentenceTransformer(model_name)
    project_embedding = model.encode([project_desc_short])[0]

    embedding_matrix = np.vstack(embeddings_df['embedding'].values)
    similarities = cosine_similarity([project_embedding], embedding_matrix)[0]

    embeddings_df['similarity'] = similarities
    top_k_df = embeddings_df.sort_values(by='similarity', ascending=False).head(top_k).reset_index(drop=True)
    return top_k_df
