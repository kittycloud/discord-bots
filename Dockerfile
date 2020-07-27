FROM python:latest

RUN apt-get update && apt-get install -y \
    curl \
    libffi-dev \
    libnacl-dev \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U discord.py[voice] && mkdir -p /app

# COPY kevin-the-cat.py /app/main.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod a+x /app/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]