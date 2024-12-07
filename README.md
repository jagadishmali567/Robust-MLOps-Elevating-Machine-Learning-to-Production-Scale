# Robust-MLOps-Elevating-Machine-Learning-to-Production-Scale

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Dataset link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset


## Git commands


```Bash
git add .

git commit -m "Updated"

git push origin main
```


## How to run?


```Bash
conda create -n usvisa python=3.8 -y
```

```Bash
source activate base
```

```Bash
conda activate usvisa
```

```Bash
pip install -r requirements.txt
```


## Project WorkFlow:

1. constants
2. entity
3. components
4. pipeline
5. Main file



## Export the environment variable:

```Bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
```

```Bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
```

```Bash
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```


## AWS CICD Deployment with Github Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

#### with specific access:

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#### Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2


#### Policy:
```Bash
1. AmazonEC2ContainerRegistryFullAccess
```
```Bash
2. AmazonEC2FullAccess
```
```Bash
3. AmazonS3FullAccess
```

### 3. Create ECR repo to store/save docker image
```Bash
Save the URI: 954976285001.dkr.ecr.us-east-1.amazonaws.com/visa
```

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine:

**optinal**

```Bash
sudo apt-get update -y
```
```Bash
sudo apt-get upgrade
```
**required**

```Bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
```Bash
sudo sh get-docker.sh
```
```Bash
sudo usermod -aG docker ubuntu
```
```Bash
newgrp docker
```


### 6. Configure EC2 as self-hosted runner:

```Bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

### 7. Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO