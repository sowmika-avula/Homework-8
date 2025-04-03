# DevOps - Automated Builds with GitHub Actions and Docker Hub

This repository demonstrates a CI/CD pipeline using GitHub Actions to automatically test, build, and push a Python application to Docker Hub.

## Project Structure

- `main.py`: Main Python application file
- `test.py`: Test files for the application
- `Dockerfile`: Container configuration
- `requirements.txt`: Python dependencies
- `.github/workflows/production.yml`: GitHub Actions workflow configuration

## CI/CD Pipeline

The pipeline consists of two main jobs:
1. **Test**: Runs Python tests using pytest
2. **Build and Push**: Creates and pushes the Docker image to Docker Hub

## Docker Hub Repository

Below is a screenshot showing the successfully published Docker image in my Docker Hub account:

![Docker Hub Repository](Screenshot%202025-04-02%20195344.png)

## Application Preview

The application is a simple Flask web server that displays a welcome message. You can run it locally using:

```bash
# Pull and run the Docker image
docker pull sowmikaavula/devops_demo:latest
docker run -d -p 5000:5000 sowmikaavula/devops_demo:latest
```

Then visit http://localhost:5000 in your browser.

## How to Run

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Build Docker image: `docker build -t your-image-name .`
5. Run container: `docker run your-image-name`