# Simple Model Manager - Project Implementation Plan

## Project Overview
A Flask-based translation service using NLLB-600M with swappable language model architecture, supporting JSON/YAML processing and translation.

## Milestone 1: Project Foundation
### Tasks:
- Initialize git repository: `git init` and `git remote add origin <repo_url>`
- Create project structure:
  ```
  simple-model-manager/
  ├── app/
  │   ├── __init__.py
  │   ├── models/
  │   ├── services/
  │   ├── routes/
  │   └── utils/
  ├── tests/
  ├── config/
  ├── requirements.txt
  ├── Dockerfile
  ├── docker-compose.yml
  ├── .env.example
  ├── .gitignore
  └── README.md
  ```
- Setup virtual environment: `python -m venv venv`
- Create base requirements.txt with Flask, pytest, pyyaml, transformers, torch
- Create comprehensive README.md with Linux/Mac installation instructions

## Milestone 2: Core Flask Application Setup
### Tasks:
- Create Flask application factory in `app/__init__.py`
- Setup configuration management in `config/settings.py`
- Environment variable handling for model selection
- Basic health check endpoint
- Application entry point in `run.py`

## Milestone 3: Language Model Service Layer
### Tasks:
- Create abstract base class `BaseTranslationModel` in `app/models/base.py`
- Implement NLLB-600M model class in `app/models/nllb.py`
- Create model factory pattern in `app/services/model_factory.py`
- Environment-based model selection logic
- Model initialization and caching service

## Milestone 4: Language Code Management
### Tasks:
- Create language code mapping in `app/utils/language_codes.py`
- Two-digit to language name dictionary
- Language validation utilities
- Supported language enumeration endpoint

## Milestone 5: File Processing Service
### Tasks:
- Create file parser service in `app/services/file_parser.py`
- JSON/YAML detection and parsing
- Recursive leaf node extraction with path tracking
- Data structure preservation for reconstruction
- File format validation

## Milestone 6: Translation Service
### Tasks:
- Create translation service in `app/services/translation_service.py`
- Prompt template management:
  ```
  "You are a translator tasked to translate a message from {source_language} to {target_language}. 
  When doing so ignore any language between the symbols #{{ and }} but use the name within as added 
  context for the translation of the other parts of the language. Translate the following: {text}"
  ```
- Batch translation processing
- Error handling and retry logic
- Translation result caching

## Milestone 7: Data Reconstruction Service
### Tasks:
- Create reconstruction service in `app/services/reconstruction_service.py`
- Path-based value replacement in original structure
- Preserve original data types and formatting
- Handle nested structures correctly

## Milestone 8: Main Translation Endpoint
### Tasks:
- Create translation route in `app/routes/translate.py`
- Parameter validation:
  - `translate_from`: two-digit language code
  - `translate_to`: two-digit language code
  - `export_format`: json|yaml
  - File upload handling
- Request/response handling
- Error response formatting

## Milestone 9: Testing Framework
### Tasks:
- Setup pytest configuration in `pytest.ini`
- Create test fixtures in `tests/conftest.py`
- Unit tests for each service layer
- Integration tests for translation endpoint
- Mock language model for testing
- Test data fixtures (sample JSON/YAML files)

## Milestone 10: Docker Configuration
### Tasks:
- Create production Dockerfile
- Multi-stage build for optimization
- Model downloading strategy
- Environment variable configuration
- Create docker-compose.yml for local development
- Health check configuration

## Milestone 11: API Documentation & Validation
### Tasks:
- Add Flask-RESTX or similar for API documentation
- Request/response schema validation
- OpenAPI specification generation
- Input sanitization and validation
- Rate limiting considerations

## Milestone 12: Error Handling & Logging
### Tasks:
- Comprehensive error handling middleware
- Structured logging with Python logging
- Translation error recovery
- File processing error handling
- Model loading error handling

## Milestone 13: Configuration & Deployment
### Tasks:
- Environment-specific configuration files
- Model path configuration
- Performance tuning parameters
- Production deployment documentation
- CI/CD pipeline setup (GitHub Actions)
- **Update README.md with final deployment instructions and troubleshooting**

## Documentation Updates per Milestone:
- **Milestone 1**: Initial README with setup instructions
- **Milestone 2**: Add Flask development server instructions
- **Milestone 8**: Add API usage examples and endpoint documentation
- **Milestone 10**: Add Docker setup and deployment instructions
- **Milestone 13**: Add production deployment and troubleshooting guide

## README.md Sections to Maintain:
1. **Prerequisites** - System requirements for Linux/Mac
2. **Installation** - Step-by-step setup for both platforms
3. **Development Setup** - Local development environment
4. **Docker Setup** - Container-based deployment
5. **API Usage** - Endpoint documentation with examples
6. **Testing** - How to run tests
7. **Troubleshooting** - Common issues and solutions
8. **Contributing** - Development guidelines

## Technical Specifications

### Environment Variables:
```
MODEL_TYPE=nllb-600m
MODEL_PATH=/models/nllb-600m
FLASK_ENV=development
LOG_LEVEL=INFO
```

### API Endpoint:
```
POST /translate
Content-Type: multipart/form-data or application/json

Parameters:
- file: JSON/YAML file
- translate_from: two-digit language code
- translate_to: two-digit language code  
- export_format: json|yaml
```

### Model Abstraction:
```python
class BaseTranslationModel:
    def translate(self, text: str, source_lang: str, target_lang: str) -> str
    def is_available(self) -> bool
    def get_supported_languages(self) -> List[str]
```

### Testing Strategy:
- Unit tests: 80%+ coverage
- Integration tests for full translation pipeline
- Performance tests for large files
- Error condition testing
- Mock external dependencies

## Deliverables by Milestone:
1. ✅ Git repository with project structure
2. ✅ Flask application with health check
3. ✅ Swappable model architecture
4. ✅ Language code management
5. ✅ File parsing capabilities
6. ✅ Translation service with prompt templating
7. ✅ Data reconstruction service
8. ✅ Working translation API endpoint
9. ✅ Complete test suite
10. ✅ Docker containerization
11. ✅ API documentation
12. ✅ Production-ready error handling
13. ✅ Deployment-ready configuration