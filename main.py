from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def root(request: Request):
    return {"Jakub Marzęda": "Aplikacja do nauki słówek z języka angielskiego"}


if __name__ == "__main__":
    uvicorn.run(app)
