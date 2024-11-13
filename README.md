
# NSFW Classifier Microservice

A sample microservice that classifies images as NSFW or neutral using a pre-trained model. It provides a REST API endpoint that accepts an image file and returns classification scores.

```
nsfw-classifier-microservice/
│
├── .devcontainer/              # Dev container configuration for VS Code
├── data/
│   └── image/                  # Folder containing images for testing
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker configuration for containerizing the app
├── nsfw_classifier.py          # Main Flask microservice code
├── nsfw_classifier.ipynb       # Notebook for interacting with the model 
├── README.md                   # This documentation
└─ requirements.txt             # Python dependencies
```
## Requirements

- Python 3.9+
- Docker (optional for containerized deployment)
- Docker Compose (optional)

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/mirceagrelus/nsfw-classifier-microservice.git
cd nsfw-classifier-microservice
```

### Install Dependencies

If running locally without Docker, create a virtual environment and install dependencies from `requirements.txt`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```


## Running the Microservice
You can
- run the service locally
- run the provided Docker image, or Docker Compose
- run inside Visual Studio Code using the provided Dev Container.

### Option 1: Run Locally

To run the service on your local machine, start the Flask app directly:

```bash
python nsfw_classifier.py
```

The microservice will be available at `http://127.0.0.1:5000/nsfw_classifier`.

### Option 2: Run with Docker

1. **Build the Docker image**:

   ```bash
   docker build -t nsfw_classifier_service .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8080:5000 nsfw_classifier_service
   ```
   This maps your local port 8080 to the port 5000 inside the docker container. 

The service will be available at `http://127.0.0.1:8080/nsfw_classifier` when accessed from the host machine.

### Option 3: Run with Docker Compose

If you prefer using Docker Compose, use the provided `docker-compose.yml` file.

1. **Start the service**:

   ```bash
   docker compose up -d
   ```

2. **Stop the service**:

   ```bash
   docker compose down
   ```

The service will be available at `http://127.0.0.1:8080/nsfw_classifier`.

### Option 4: Run inside Visual Studio Code using DevContainers
1. **Install the DevContainers extension for VSCode - if not installed.**
2. **Open the project folder in VSCode**
3. **Select the Dev Containers option to `Reopen in container`**

## First run
On first run download the model locally. I haven't included it to save space.

Uncomment the lines to download the model:
```python
pipe = pipeline("image-classification", model="giacomoarienti/nsfw-classifier")
pipe.save_pretrained(local_model_path)
```

### Example Request

To test the API using `curl`, use the following command:

```bash
curl -X POST -F "image=@path/to/your/image.png" http://127.0.0.1:8080/nsfw_classifier
```

### Example Response

```json
{
    "neutral_score": 0.85,
    "porn_score": 0.15
}
```

## Project Structure

- **nsfw_classifier.py**: The main microservice code.
- **requirements.txt**: Python dependencies.
- **Dockerfile**: Docker setup for containerized deployment.
- **docker-compose.yml**: Docker Compose file for running the service.

