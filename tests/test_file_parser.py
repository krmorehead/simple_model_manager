import pytest
from app.services.file_parser import FileParser

@pytest.fixture
def parser() -> FileParser:
    return FileParser()

def test_detect_format_stub(parser: FileParser) -> None:
    assert parser.detect_format('{"a": 1}') == ''
    assert parser.detect_format('a: 1') == ''

def test_parse_stub(parser: FileParser) -> None:
    assert parser.parse('{"a": 1}') is None
    assert parser.parse('a: 1') is None

def test_extract_leaf_nodes_stub(parser: FileParser) -> None:
    assert parser.extract_leaf_nodes({"a": 1}) == []
    assert parser.extract_leaf_nodes([1, 2, 3]) == []

def test_is_valid_format_stub(parser: FileParser) -> None:
    assert parser.is_valid_format('{"a": 1}') is False
    assert parser.is_valid_format('a: 1') is False

def test_sample_json_file_fixture(sample_json_file) -> None:
    content = sample_json_file.read().decode('utf-8')
    assert isinstance(content, str)
    assert 'a' in content

def test_sample_yaml_file_fixture(sample_yaml_file) -> None:
    content = sample_yaml_file.read().decode('utf-8')
    assert isinstance(content, str)
    assert 'a' in content 