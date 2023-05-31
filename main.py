from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db import DataBase
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#TO DO:
#Usprawnić dodawanie slowa automatycznie a nie z palca do funkcji
#Dodać template na złą odpowiedz i dobrą żeby nie był to zwykly json tylko żeby to jakoś wyglądało
#Przejrzeć kod poprawić błędy jak są(Opcjonalnie)

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request, "polish_word": "pies"})


@app.post("/")
async def get_word(request: Request):
    db = DataBase()
    form = await request.form()
    answer = form.get("word")
    if check_correct_answer_word(answer, "pies"):
        return {"Jest git"}
    else:
        return {"Podałeś złe słowo"}

def check_correct_answer_word(answer, polish_word):
    db = DataBase()
    if answer == db.select_english_word(polish_word):
        return True
    else:
        return False


if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload")
