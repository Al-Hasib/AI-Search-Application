# Build the Docker image
docker build -t fastapi-app .

# Run the container
docker run -p 8000:8000 fastapi-app