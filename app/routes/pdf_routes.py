from fastapi import APIRouter, Form, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from app.utils.pdf_generator import generate_pdf
import uuid
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/generate-pdf/")
async def generate_pdf_from_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join("app", "static", filename)
    generate_pdf(name, email, message, filepath)
    return templates.TemplateResponse("form.html", {
        "request": request,
        "pdf_url": f"/static/{filename}"
    })
