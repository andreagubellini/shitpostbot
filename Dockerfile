FROM python:3.8-slim-buster

RUN mkdir src
RUN mkdir config
COPY src/ src/
COPY config/ config/
COPY requirements.txt   /
RUN pip3 install -r requirements.txt

CMD ["python3", "src/bot.py", "-f", "config/config_ex.yml"]
