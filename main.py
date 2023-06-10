from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from db import DataBase
import random
import os

app = FastAPI()
id = random.randrange(1, 31)
iteration = 0
good_answer = 0
user = ""
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# TO DO:
# Dodać autoryzację do poszczególnych endpointów
# Dodać porównanie każdego zajerestrowanego użytkownika i jego ilość bezbłędnych nauczonych słówek albo odwrotnie(dla kazdego użytkownika dana)
# Zmienić losowanie liczby żeby każdy random był inny czyli bez powtarzania

# Wygenerowania strony do zalogowania za pomocą get'a
@app.get("/login")
def generate_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": ""})


# Przechwycenie danych z formularza logowania za pomoca post'a i sprawdzenia czy użytkownik istnieje w bazie funckją check_login_user
@app.post("/login")
async def get_login_data(request: Request):
    db = DataBase()
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    result = db.check_login_user(email, password)
    if db.check_login_admin(password):
        return RedirectResponse(url='/admin_panel', status_code=status.HTTP_303_SEE_OTHER)
    else:
        if result:
            global iteration
            global user
            global good_answer
            user = result[0][0]
            iteration = 0
            good_answer = 0
            return RedirectResponse(url='/installing', status_code=status.HTTP_303_SEE_OTHER)
        else:
            return RedirectResponse(url='/register', status_code=status.HTTP_303_SEE_OTHER)


# Wygenerowanie strony do zajerestrowania za pomocą get'a
@app.get("/register")
def generate_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# Przechwycenie danych z formularza do rejestracji i zajerestrowanie(funckja insert_user_data) i przeniesienie go na endpoint do logowania
@app.post("/register")
async def get_register_data(request: Request):
    db = DataBase()
    form = await request.form()
    name = form.get("name")
    lastname = form.get("lastname")
    email = form.get("email")
    password = form.get("password")

    try:
        db.insert_user_data(name, lastname, email, password)
        return RedirectResponse(url='/login', status_code=status.HTTP_303_SEE_OTHER)
    except Exception:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Wrong data"})


# Wygenerowanie głównej strony do nauki słówek za pomocą get'a
@app.get("/installing")
def generate_installing_page(request: Request):
    global id
    id = random.randrange(1, 31)
    db = DataBase()
    polish_word = db.select_polish_word(id)
    sentence_with_gap = db.select_sentence_with_gap(id)
    return templates.TemplateResponse("main_page.html", {"request": request, "polish_word": polish_word,
                                                         "sentence_with_gap": sentence_with_gap})


# Przechwycenie odpowiedzi od użytkownika i sprawdzenie czy jest ok(check_correct_answer_word) następnie wyświetlenie odpowiedzi
@app.post("/installing")
async def get_word(request: Request):
    global iteration
    global good_answer
    global user
    form = await request.form()
    answer = form.get("word")
    sentence_without_gap, english_word, polish_word = data_for_results(id)
    if check_correct_answer_word(answer, id):
        good_answer += 1
        iteration += 1
        result = check_iteration_limit(iteration)
        if result:
            db = DataBase()
            db.insert_user_progress(good_answer, user)
            return result
        return templates.TemplateResponse("good_result.html",
                                          {"request": request, "sentence_without_gap": sentence_without_gap,
                                           "english_word": english_word, "polish_word": polish_word})
    else:
        iteration += 1
        result = check_iteration_limit(iteration)
        if result:
            return result
        return templates.TemplateResponse("bad_result.html",
                                          {"request": request, "sentence_without_gap": sentence_without_gap,
                                           "english_word": english_word, "polish_word": polish_word})


# Wygenerowanie panela administratora który ma podgląd na użytkowników oraz możliwość dodania słówek
@app.get("/admin_panel")
def generate_admin_page(request: Request):
    db = DataBase()
    users = db.display_users()
    return templates.TemplateResponse("admin_panel.html", {"request": request, "users": users})


# Przechwycenie danych które są potrzebne do wstawienia słówka do bazy które jest dodane przez admina
@app.post("/admin_panel")
async def get_word_to_add_database(request: Request):
    db = DataBase()
    form = await request.form()
    polish_word = form.get("polish_word")
    english_word = form.get("english_word")
    sentence_with_gap = form.get("sentence_with_gap")
    sentence_without_gap = form.get("sentence_without_gap")
    db.insert_word(polish_word, english_word, sentence_with_gap, sentence_without_gap)
    return {"Dodano słówko do bazy"}


# Wygenerowanie strony do wyświetlenia wyniku ile słówek udało się zrobić bezbłędnie
@app.get("/result")
def generate_result_page(request: Request):
    return templates.TemplateResponse("result.html", {"request": request, "good_answer": good_answer, "user": user})


# Sprawdzenie czy słówko podane przez usera jest poprawne
def check_correct_answer_word(answer, id):
    db = DataBase()
    return answer == db.select_english_word(id)


# Wyciągnięcie z bazy słowa po polsku, angielsku oraz zdania po danym id
def data_for_results(id):
    db = DataBase()
    sentence_without_gap = db.select_sentence_without_gap(id)
    english_word = db.select_english_word(id)
    polish_word = db.select_polish_word(id)
    return sentence_without_gap, english_word, polish_word


# Sprawdzenie ile razy użytkownik już podał słówko aby ograniczyć go do nauki 20 słówek
def check_iteration_limit(iteration):
    if iteration == 20:
        return RedirectResponse(url='/result', status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload")
