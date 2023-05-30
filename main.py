from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

@app.post("/")
async def get_word(request: Request):
    form = await request.form()
    word = form.get("word")
    print(word)

if __name__ == "__main__":
    uvicorn.run(app)
