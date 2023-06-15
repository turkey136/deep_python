FROM python:3.9

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip

WORKDIR /home/DeepLearning
COPY requirements.txt ${PWD}

RUN pip install -r requirements.txt

WORKDIR /home/DeepLearning/src
