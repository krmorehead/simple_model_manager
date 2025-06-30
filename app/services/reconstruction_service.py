from typing import Any, Dict, List, Tuple, Union

class ReconstructionService:
    """
    Service for reconstructing data structures by replacing values at given paths, preserving types and formatting.
    """
    def replace_values(self, data: Union[Dict[str, Any], List[Any]], replacements: List[Tuple[str, Any]]) -> Union[Dict[str, Any], List[Any]]:
        """
        Replaces values in the data structure at the specified paths.
        Args:
            data (Union[Dict, List]): The original data structure.
            replacements (List[Tuple[str, Any]]): List of (path, value) pairs to replace.
        Returns:
            Union[Dict, List]: The reconstructed data structure.
        """
        def set_by_path(obj, path, value):
            parts = []
            for p in path.replace(']', '').split('.'):
                if '[' in p:
                    k, *idxs = p.split('[')
                    if k:
                        parts.append(k)
                    parts.extend(int(i) for i in idxs if i)
                else:
                    parts.append(p)
            ref = obj
            for p in parts[:-1]:
                if isinstance(p, int):
                    ref = ref[p]
                else:
                    ref = ref[p]
            last = parts[-1]
            if isinstance(last, int):
                ref[last] = value
            else:
                ref[last] = value
        for path, value in replacements:
            set_by_path(data, path, value)
        return data

    def preserve_types_and_formatting(self, original: Any, new_value: Any) -> Any:
        """
        Preserves the type and formatting of the original value when replacing.
        Args:
            original (Any): The original value.
            new_value (Any): The new value to insert.
        Returns:
            Any: The value with preserved type/formatting (stub).
        """
        return new_value 