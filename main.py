from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db import DataBase
import random
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# TO DO:
# Usprawnić dodawanie slowa automatycznie a nie z palca do funkcji
# Dodać template na złą odpowiedz i dobrą żeby nie był to zwykly json tylko żeby to jakoś wyglądało
# Przejrzeć kod poprawić błędy jak są(Opcjonalnie)
id = random.randrange(1, 31)


@app.get("/")
def root(request: Request):
    db = DataBase()
    polish_word = db.select_polish_word(id)
    sentence_with_gap = db.select_sentence_with_gap(id)
    return templates.TemplateResponse("main_page.html", {"request": request, "polish_word": polish_word,
                                                         "sentence_with_gap": sentence_with_gap})


@app.post("/")
async def get_word(request: Request):
    form = await request.form()
    answer = form.get("word")
    sentence_without_gap, english_word, polish_word = data_for_results(id)
    if check_correct_answer_word(answer, id):
        return templates.TemplateResponse("good_result.html", {"request": request, "sentence_without_gap": sentence_without_gap, "english_word": english_word, "polish_word": polish_word})
    else:
        return templates.TemplateResponse("bad_result.html", {"request": request, "sentence_without_gap": sentence_without_gap, "english_word": english_word, "polish_word": polish_word})


def check_correct_answer_word(answer, id):
    db = DataBase()
    if answer == db.select_english_word(id):
        return True
    else:
        return False


def data_for_results(id):
    db = DataBase()
    sentence_without_gap = db.select_sentence_without_gap(id)
    english_word = db.select_english_word(id)
    polish_word = db.select_polish_word(id)
    return sentence_without_gap, english_word, polish_word


if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload")
