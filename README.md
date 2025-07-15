# AdHocMatch

**Scalable Reviewer and Consultant Recommendation via Semantic Filtering and LLM-Based Digital Twins**

AdHocMatch is a hybrid system designed to automate and scale the recommendation of reviewers or consultants (AdHoc evaluators) for projects, proposals, or tasks. It combines fast semantic filtering with contextual evaluations powered by Large Language Models (LLMs), simulating each top-k candidate as a "digital twin".

## 🚀 Overview

The system operates in two main stages:

1. **Semantic Filtering** — Uses sentence embeddings to match project summaries with consultant profiles, identifying the top-k most relevant candidates.
2. **LLM-Based Evaluation** — For each of the top-k candidates, a custom LLM prompt is created using their profile, allowing a personalized agent (digital twin) to assess project affinity, justification, topic overlap, conflicts of interest, and suggested role.

The final output is a structured and interpretable JSON file with ranked recommendations for each project.

## 📦 Features

* Two-stage architecture balancing speed and reasoning depth
* Support for multilingual sentence embeddings (e.g., `paraphrase-multilingual-mpnet-base-v2`)
* Pluggable LLM providers (tested with [OpenRouter](https://openrouter.ai))
* Structured JSON outputs for auditability and integration
* Modular Python package structure (`pip install -e .`)
* Ready-to-use synthetic test data and prompts

## 🔧 Configuration (`config.yaml`)

```yaml
llm_provider: "openrouter"
llm_model: "meta-llama/llama-4-scout"
llm_endpoint: "https://openrouter.ai/api/v1"
llm_api_key: "sk-...your_api_key..."

sentence_transformer_model: "paraphrase-multilingual-mpnet-base-v2"

top_k: 2

projects_file: "data/projects.json"
consultants_file: "data/consultants.json"
consultants_embeddings_file: "data/consultants_with_embeddings.parquet"

system_prompt_folder: "prompts/"
output_scores_file: "output/top_consultants.json"
```

> 💡 If the `consultants_with_embeddings.parquet` file is missing or out of sync with the current consultant list, the embeddings will be automatically regenerated and saved.

## 📁 Folder Structure

```
.
├── adhocmatch/                 # Core Python package
│   ├── embeddings.py
│   ├── evaluation.py
│   ├── llm_agent.py
│   ├── main.py
│   └── utils.py
├── data/                       # Input data (projects, consultants)
├── output/                     # Generated output JSON
├── prompts/                   # System prompt templates
├── config.yaml                # YAML configuration file
├── requirements.txt
└── README.md
```

## ▶️ Usage in Python (e.g., Colab)

```python
from adhocmatch.main import run_pipeline
from adhocmatch.utils import load_config

config = load_config("config.yaml")
run_pipeline(config)
```

## 📄 Output Format

For each project, the output includes:

```json
{
  "project_id": "p001",
  "consultant_id": "c012",
  "affinity_score": 0.85,
  "justification": "...",
  "topics_overlap": ["AI", "text mining"],
  "possible_conflicts": [],
  "suggested_role": "AdHoc Reviewer"
}
```

## 📚 Applications

* Assignment of AdHoc reviewers in academic and funding programs
* Project-consultant matching in government and NGOs
* Team formation and HR recommendation
* Expert selection in public/private sector innovation programs

## 🧠 Citation & Paper

This tool is based on the paper:

> *AdHocMatch: Scalable Reviewer Recommendation with Semantic Filtering and LLM-Based Digital Twins*
> \[preprint coming soon]

## ✅ License

MIT License. Feel free to adapt and use in your institution.
