# Simple Model Manager

## Prerequisites
- Python 3.8+
- pip
- (Recommended) virtualenv or venv
- Git
- Linux or MacOS

## Installation

### 1. Clone the repository
```bash
git clone <repo_url>
cd language_model_simple
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Development Setup
- All source code is in the `app/` directory.
- Tests are in the `tests/` directory.
- Configuration files are in the `config/` directory.

## Docker Setup
To run the app in Docker and expose it on port 7000:
```bash
docker-compose up --build
```
Then access the app at http://localhost:7000

## Production Deployment
- Set environment variables in a `.env` file or via your deployment platform.
- Build and run the Docker container:
  ```bash
  docker-compose -f docker-compose.yml up --build -d
  ```
- Access the app at http://localhost:7000

## Environment Variables
- See `.env.example` for all supported variables.

## Troubleshooting
- Check logs for errors (`docker-compose logs` or container logs).
- Ensure all environment variables are set correctly.
- For model download issues, verify model path and permissions.
- For port conflicts, change the `ports` mapping in `docker-compose.yml`.

## CI/CD
- Recommended: Set up GitHub Actions for automated testing and deployment.

## Next Steps
- See the project plan for further milestones and instructions.
