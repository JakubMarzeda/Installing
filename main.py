from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def root(request: Request):
    return {"Jakub Marzęda": "Aplikacja do nauki słówek z języka angielskiego"}


@app.get("/name")
def get_name(request: Request):
    return {"Name": request}


if __name__ == "__main__":
    uvicorn.run(app)
