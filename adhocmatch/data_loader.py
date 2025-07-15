
import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any

def load_project(project_path: str) -> Dict[str, Any]:
    path = Path(project_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de projeto não encontrado: {project_path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_projects(projects_path: str) -> List[Dict[str, Any]]:
    path = Path(projects_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de projetos não encontrado: {projects_path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_consultants(consultants_path: str) -> List[Dict[str, Any]]:
    path = Path(consultants_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de consultores não encontrado: {consultants_path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_embeddings_if_exist(embeddings_path: str, consultants: List[Dict[str, Any]]) -> pd.DataFrame:
    path = Path(embeddings_path)
    if not path.exists():
        return None

    try:
        df = pd.read_parquet(path)
        embedded_ids = sorted(df["consultant_id"].tolist())
        current_ids = sorted([c["consultant_id"] for c in consultants])

        if embedded_ids != current_ids:
            print("⚠️ IDs de consultores não batem com os embeddings. Ignorando cache.")
            return None

        return df

    except Exception as e:
        print(f"❌ Erro ao carregar embeddings: {e}")
        return None