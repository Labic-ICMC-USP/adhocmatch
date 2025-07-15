
import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path='config.yaml'):
        self.config_path = Path(config_path)
        self.data = self._load_config()

    def _load_config(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)
