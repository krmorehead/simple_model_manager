# API Reference

## Overview
This document describes the API endpoints for the Simple Model Manager project.

## Endpoints
- `POST /translate`: Main translation endpoint.
  - **Request (JSON):** `{ "text": str, "source_lang": str, "target_lang": str }`
  - **Request (multipart/form-data):** file (JSON/YAML), `translate_from`, `translate_to`, `export_format`
  - **Response (JSON):** `{ "translation": str }`
  - **Response (file):** `{ "result": str }` (stub)
  - **Error Responses:**
    - 400: `{ "error": "Missing required fields" }`, `{ "error": "Invalid language code" }`, `{ "error": "Invalid export format" }`, `{ "error": "Invalid file format" }`
    - 500: `{ "error": "Internal server error" }`
  - Calls the `ModelService.translate` method (currently stubbed).
- `GET /languages`: Returns a list of supported language codes and names.
  - **Response JSON:** `{ "languages": [{ "code": str, "name": str }, ...] }`
  - **Error Responses:**
    - 500: `{ "error": "Internal server error" }`

This file will be updated as endpoints are added and evolve. 