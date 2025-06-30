import pytest
from app.services.reconstruction_service import ReconstructionService

@pytest.fixture
def service() -> ReconstructionService:
    return ReconstructionService()

def test_replace_values_stub(service: ReconstructionService) -> None:
    data = {"a": 1}
    replacements = [("a", 2)]
    assert service.replace_values(data, replacements) == data

def test_preserve_types_and_formatting_stub(service: ReconstructionService) -> None:
    assert service.preserve_types_and_formatting(1, "2") == "2" 