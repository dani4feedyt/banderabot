import psycopg2
import os
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import json
import yaml

load_dotenv()

engine = psycopg2.connect(
    database="postgres",
    user=f"{os.getenv('DB_USER')}",
    password=f"{os.getenv('DB_PASSWORD')}",
    host=f"{os.getenv('DB_HOST')}",
    port=f"{os.getenv('DB_PORT')}",
)

cur = engine.cursor(cursor_factory=DictCursor)

with open("textual.yml", "r", encoding="utf-8") as f:
    textual = yaml.safe_load(f)

with open("functional.json", "r", encoding="utf-8") as f:
    functional = json.load(f)
