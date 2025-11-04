# Medical-chatbot

[![CI/CD](https://github.com/Joab-David-Johanan/Medical-chatbot/actions/workflows/cicd.yaml/badge.svg)](https://github.com/Joab-David-Johanan/Medical-chatbot/actions)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20ECR-orange)
![MLOps](https://img.shields.io/badge/MLOps-CI%2FCD%20pipeline-yellow)

This repo is used to create a medical chatbot using a RAG pipeline.

## Techstack used:

- Python
- Langchain
- Pinecone
- OpenAI models
- Flask

## Steps to run the program:

### 1. Create and clone the repository

```bash
git clone https://github.com/Joab-David-Johanan/Medical-chatbot
```

### 2. Create a conda environment after opening the repository

```bash
conda create -n medibot python==3.12 -y
```

```bash
conda activate medibot
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory and add your pinecone and openai credentials as follows:

```bash
PINECONE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXX"
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXX"

```

```bash
# run the following command to store the embeddings to pinecone
python store_index.py
```

```bash
# Finally run the Flask app
python app.py
```

## Deployment steps:

### 1. Log-in to AWS console.

### 2. Create IAM user for deployment

      # with specific access
      1. EC2 access: For setting up a virtual server.
      2. ECR access: Elastic container registry to save your docker image in aws.

      # Policy
      1. AmazonEC2ContainerRegistryFullAccess
      2. AmazonEC2FullAccess

      # Description: About the deployment
      1. Build Docker image of the source code.
      2. Push your Docker image to ECR.
      3. Launch your EC2.
      4. Pull your Docker image from ECR to EC2.
      5. Launch your Docker image in EC2.

### 3. Create ECR repo to store/save Docker image

```bash
# Save the URI
454041007932.dkr.ecr.us-east-1.amazonaws.com/medical-bot
```

### 4. Create a EC2 instance (Ubuntu)

      # Allow HTTPS and HTTP traffic.
      # Choose 8gb instance (t2.large).
      # Choose 30gb storage.

### 5. Launch the EC2 instance and install Docker in the EC2 instance

1. optional

```bash
sudo apt-get update -y
```

```bash
sudo apt-get upgrade
```

2. required

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
sudo sh get-docker.sh
```

```bash
sudo usermod -aG docker ubuntu
```

```bash
newgrp docker
```

### 6. Configure EC2 instance as a self-hosted runner

      settings-->actions-->runner-->new self hosted runner-->choose os-->then run command one by one

### 7. Setup Github secrets

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO_NAME
- PINECONE_API_KEY
- OPENAI_API_KEY

### 8. Ensure conditional integration and deployment with tags

1. Make sure all your changes (including YAML) are committed

```bash
git add .
git commit -m "Initial commit with CI/CD"
```

2. Push your code to GitHub

```bash
git push origin main
```

3. Create a version tag for deployment

```bash
git tag -a v1.0.0 -m "Initial release"
```

4. Push that tag to GitHub (triggers deployment)

```bash
git push origin v1.0.0
```

### 9. Features to include

- Advanced chunking techniques
- Hybrid search strategies
- Query Enhancement techniques
- Multimodal RAG techniques
- Guardrails
- Cache for faster response times
- Custom Javascript frontend with python backend (flask)
