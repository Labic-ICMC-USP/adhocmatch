import json
from typing import Dict, Any, List, Callable

def run_affinity_evaluation(evaluator_fn: Callable[[str], str], project_desc_full: str) -> Dict[str, Any]:
    try:
        response = evaluator_fn(project_desc_full)
        return json.loads(response.replace("```json","").replace("```",""))
    except Exception as e:
        print(e)
        return {
            "affinity_score": 0.0,
            "justification": f"Erro durante a avaliação: {e}",
            "topics_overlap": [],
            "possible_conflicts": [],
            "suggested_role": "N/A"
        }

def evaluate_top_k(project: Dict[str, Any], consultants: List[Dict[str, Any]], evaluators: List[Callable[[str], str]]) -> List[Dict[str, Any]]:
    results = []
    for consultant, evaluator_fn in zip(consultants, evaluators):
        result = run_affinity_evaluation(evaluator_fn, project['desc_full'])
        result['consultant_id'] = consultant['consultant_id']
        results.append(result)
    return results
