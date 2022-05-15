from os import environ

from dotenv import load_dotenv
from uvicorn import run

if __name__ == "__main__":
    load_dotenv()
    run("api:api", host=environ.get("HOST"), port=8000, reload=True)
