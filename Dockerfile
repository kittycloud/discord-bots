FROM python:latest

RUN apt-get update && apt-get install -y \
    curl \
    libffi-dev \
    libnacl-dev \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U discord.py[voice]

RUN mkdir -p /app && curl https://raw.githubusercontent.com/kittycloud/discord-bots/master/kevin-the-cat.py -o /app/main.py

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]