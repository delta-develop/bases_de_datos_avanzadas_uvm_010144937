from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from handlers import save_to_xml, write_to_html

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/process-form", response_class=RedirectResponse, status_code=302)
async def profess_form(
    id: Annotated[str, Form()],
    name: Annotated[str, Form()],
    lastname: Annotated[str, Form()],
    age: Annotated[str, Form()],
    sex: Annotated[str, Form()],
    position: Annotated[str, Form()],
):
    
    data = {
        "empleoyee":{
            "id":id,
            "name":name,
            "lastname":lastname,
            "age":age,
            "sex":sex,
            "position":position
        }

    }

    save_to_xml(data)

    return "/show-table"

@app.get("/show-table", response_class=HTMLResponse)
async def show_table(request: Request):
    write_to_html()
    return templates.TemplateResponse("output.html", {"request":request})
