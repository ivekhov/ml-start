from fastapi import FastAPI
from datetime import date, timedelta

app = FastAPI()


@app.get("/")
def hello():
    return 'hello'


@app.get("/sum_date")
def sum_date(current_date: date, offset: int) -> str:
    date_incremented = current_date + timedelta(days=offset)
    result = date_incremented.isoformat()
    return result
