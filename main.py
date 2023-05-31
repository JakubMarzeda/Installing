from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db import DataBase
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request, "polish_word": "pies"})


@app.post("/")
async def get_word(request: Request):
    form = await request.form()
    word = form.get("word")
    if check_word(word, "pies"):
        return {"Jest git"}
    else:
        return {"Podałeś złe słowo"}


def check_word(english_word, polish_word):
    if english_word == db.select_english_word(polish_word):
        return True
    else:
        return False


if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload")
