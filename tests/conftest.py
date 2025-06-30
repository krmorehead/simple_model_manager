import pytest
import io

@pytest.fixture
def sample_json_file() -> io.BytesIO:
    return io.BytesIO(b'{"a": 1, "b": {"c": 2}}')

@pytest.fixture
def sample_yaml_file() -> io.BytesIO:
    return io.BytesIO(b'a: 1\nb:\n  c: 2\n') 