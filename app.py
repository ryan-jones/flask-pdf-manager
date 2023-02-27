import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
db_url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(db_url)


@app.
