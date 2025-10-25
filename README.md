# Medical-chatbot

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

      # Description: About the deployment
      1. Build Docker image of the source code.
      2. Push your Docker image to ECR.
      3. Launch your EC2.
      4. Pull your Docker image from ECR to EC2.
      5. Launch your Docker image in EC2.

      # Policy
      1. AmazonEC2ContainerRegistryFullAccess
      2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save Docker image

```bash
# Save the URI
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

### 4. Create a EC2 instance (Ubuntu)

      # Allow HTTPS requests.
      # Choose 8gb machine.
      # Choose 30gb storage.

### 5. Launch the EC2 instance and install Docker in the EC2 instance

```bash
# optional
sudo apt-get update -y
```

```bash
# optional
sudo apt-get upgrade
```

```bash
# required
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
# required
sudo sh get-docker.sh
```

```bash
# required
sudo usermod -aG docker ubuntu
```

```bash
# required
newgrp docker
```

### 6. Configure EC2 instance as a self-hosted runner:

      settings-->actions-->runner-->new self hosted runner-->choose os-->then run command one by one
