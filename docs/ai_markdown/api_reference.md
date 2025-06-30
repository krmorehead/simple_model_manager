# API Reference

## Overview
This document describes the API endpoints for the Simple Model Manager project.

## Endpoints
- `POST /translate`: Main translation endpoint.
  - **Request JSON:** `{ "text": str, "source_lang": str, "target_lang": str }`
  - **Response JSON:** `{ "translation": str }`
  - **Error Responses:**
    - 400: `{ "error": "Missing field: ..." }`
    - 500: `{ "error": "Internal server error" }`
  - Calls the `ModelService.translate` method (currently stubbed).

This file will be updated as endpoints are added and evolve. 