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

## API Endpoint Tests
- `tests/test_translate_route.py`: Unit tests for `/translate` endpoint, including valid requests, missing fields, and error handling using Flask's test client and monkeypatching.

This file will be updated as the test suite evolves. 