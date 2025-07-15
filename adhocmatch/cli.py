
from adhocmatch.config import Config
from adhocmatch.data_loader import load_project, load_consultants, load_embeddings_if_exist
from adhocmatch.embeddings import generate_embeddings, save_embeddings
from adhocmatch.matching import get_top_k_consultants
from adhocmatch.agents import create_agent
from adhocmatch.evaluation import evaluate_top_k

import json
from pathlib import Path

def main():
    print("🚀 Iniciando o sistema AdHocMatch")

    # Carrega configuração
    config = Config()
    top_k = config.get("top_k", 5)

    # Carrega dados
    project = load_project(config.get("input_project_file"))
    consultants = load_consultants(config.get("consultants_file"))
    embeddings_df = load_embeddings_if_exist(config.get("consultants_embeddings_file"))

    # Gera embeddings, se necessário
    if embeddings_df is None:
        print("📌 Nenhum embedding encontrado. Gerando agora...")
        embeddings_df = generate_embeddings(consultants, config.get("sentence_transformer_model"))
        save_embeddings(embeddings_df, config.get("consultants_embeddings_file"))
    else:
        print("✅ Embeddings encontrados e carregados.")

    # Recupera top-k consultores
    top_k_df = get_top_k_consultants(
        project_desc_short=project['desc_short'],
        embeddings_df=embeddings_df,
        model_name=config.get("sentence_transformer_model"),
        top_k=top_k
    )

    top_k_consultants = [c for c in consultants if c['consultant_id'] in top_k_df['consultant_id'].values]
    prompt_path = str(Path(config.get("system_prompt_folder")) / "base_prompt.txt")

    # Instancia agentes
    agents = [
        create_agent(c, prompt_path, config.data)
        for c in top_k_consultants
    ]

    # Avalia afinidade
    results = evaluate_top_k(project, top_k_consultants, agents)

    # Salva resultados
    output_path = config.get("output_scores_file")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"✅ Recomendações salvas em {output_path}")
