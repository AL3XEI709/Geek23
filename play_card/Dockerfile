FROM python:slim

RUN apt-get update && apt-get install socat -y
RUN pip install pycryptodome
RUN mkdir /app

WORKDIR /app

COPY play_card.py .
COPY secret.py .
COPY cards.py .

CMD ["/bin/sh", "-c", "socat TCP-LISTEN:4953,fork,reuseaddr EXEC:'python play_card.py',stderr"]