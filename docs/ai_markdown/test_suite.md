# Test Suite Documentation

## Overview
This document describes the testing strategy for the Simple Model Manager project.

- Unit tests for all public functions
- Integration tests for the translation pipeline
- Mocking of external dependencies
- 80%+ code coverage target

## Test Structure
- All tests are located in the `tests/` directory.
- Test fixtures and sample data are included for comprehensive coverage.

## Service Layer Tests
- `tests/test_model_service.py`: Unit tests for `ModelService` initialization and stubbed `translate` method.

## Language Code Utility Tests
- `tests/test_model_service.py`: Unit tests for language code validation, supported language enumeration, and name lookup.

## API Endpoint Tests
- `tests/test_translate_route.py`: Unit tests for `/translate` endpoint, including valid requests, missing fields, and error handling using Flask's test client and monkeypatching.
- `tests/test_translate_route.py`: Unit test for `/languages` endpoint, verifying correct response and content.

## File Parser Service Tests
- `tests/test_file_parser.py`: Unit tests for `FileParser` stubs, covering format detection, parsing, leaf extraction, and validation methods.

## Translation Service Tests
- `tests/test_translation_service.py`: Unit tests for `TranslationService` stubs, covering prompt building, batch translation, error handling, and caching methods.

## Reconstruction Service Tests
- `tests/test_reconstruction_service.py`: Unit tests for `ReconstructionService` stubs, covering value replacement and type/formatting preservation methods.

This file will be updated as the test suite evolves. 