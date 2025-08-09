FROM python:3.9-slim

WORKDIR /Banderabot


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Bandera_bot.py"]