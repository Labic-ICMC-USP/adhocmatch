from pathlib import Path
from langchain_openai import ChatOpenAI
from typing import Dict

def build_system_prompt(consultant_full_desc: str, base_prompt_path: str) -> str:
    prompt_base = Path(base_prompt_path).read_text(encoding='utf-8')
    return prompt_base.replace("{{CONSULTANT_DESC_FULL}}", consultant_full_desc)

def create_llm(consultant: dict, base_prompt_path: str, llm_config: dict) -> ChatOpenAI:
    system_prompt = build_system_prompt(consultant['desc_full'], base_prompt_path)

    llm = ChatOpenAI(
        base_url=llm_config['llm_endpoint'],
        api_key=llm_config['llm_api_key'],
        model=llm_config['llm_model']
    )

    # Envolve a LLM em uma função que já traz o system_prompt configurado
    def evaluator(user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = llm.invoke(messages)
        return response.content

    return evaluator
