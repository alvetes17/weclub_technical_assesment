from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

star_wars_db = [
    {"id": 1, "name": "Luke Skywalker", "role": "Jedi"},
    {"id": 2, "name": "Darth Vader", "role": "Sith Lord"},
    {"id": 3, "name": "Leia Organa", "role": "Princess"},
    {"id": 4, "name": "Han Solo", "role": "Smuggler"},
]
