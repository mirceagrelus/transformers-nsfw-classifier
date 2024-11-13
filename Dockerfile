# Start with an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker layer caching
COPY requirements.txt /app/

# Install dependencies
# RUN pip install --no-cache-dir flask transformers pillow
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure the model folder exists in the container
RUN mkdir -p ./model/nsfw-classifier

# Download the model to the container (uncomment if model is not in the project)
# RUN python -c "from transformers import pipeline; pipe = pipeline('image-classification', model='giacomoarienti/nsfw-classifier'); pipe.save_pretrained('./model/nsfw-classifier')"

# Expose port 5000
EXPOSE 5000

# Run the Flask server
CMD ["python", "nsfw_classifier.py"]