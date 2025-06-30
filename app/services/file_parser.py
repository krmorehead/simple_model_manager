from typing import Any, Dict, List, Tuple, Union
import json
import yaml

class FileParser:
    """
    Service for detecting, parsing, and extracting data from JSON/YAML files.
    """
    def detect_format(self, content: str) -> str:
        try:
            json.loads(content)
            return 'json'
        except Exception:
            pass
        try:
            yaml.safe_load(content)
            return 'yaml'
        except Exception:
            pass
        return ''

    def parse(self, content: str) -> Union[Dict[str, Any], List[Any], None]:
        fmt = self.detect_format(content)
        try:
            if fmt == 'json':
                return json.loads(content)
            elif fmt == 'yaml':
                return yaml.safe_load(content)
        except Exception:
            return None
        return None

    def extract_leaf_nodes(self, data: Union[Dict[str, Any], List[Any]], path: str = '') -> List[Tuple[str, Any]]:
        leaves = []
        if isinstance(data, dict):
            for k, v in data.items():
                new_path = f'{path}.{k}' if path else k
                if isinstance(v, (dict, list)):
                    leaves.extend(self.extract_leaf_nodes(v, new_path))
                else:
                    leaves.append((new_path, v))
        elif isinstance(data, list):
            for idx, v in enumerate(data):
                new_path = f'{path}[{idx}]' if path else f'[{idx}]'
                if isinstance(v, (dict, list)):
                    leaves.extend(self.extract_leaf_nodes(v, new_path))
                else:
                    leaves.append((new_path, v))
        return leaves

    def is_valid_format(self, content: str) -> bool:
        return self.detect_format(content) in ('json', 'yaml') 