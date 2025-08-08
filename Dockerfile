FROM python:3.9-slim

WORKDIR /Banderabot

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "Bandera_bot.py"]