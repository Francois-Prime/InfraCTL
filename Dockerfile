FROM python:3.12-slim

RUN apt-get update && apt-get install -y wget unzip \
 && wget https://releases.hashicorp.com/terraform/1.6.6/terraform_1.6.6_linux_amd64.zip \
 && unzip terraform_1.6.6_linux_amd64.zip -d /usr/local/bin

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "infractl.cli"]