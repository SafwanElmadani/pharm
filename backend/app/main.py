from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from database import Product
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="frontend")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/", response_class=HTMLResponse)
# def read_form(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
@app.get("/", response_class=HTMLResponse)
def read_form(request: Request, db: Session = Depends(get_db)):
    print("query the database")
    products = db.query(Product).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products
    })

@app.post("/add")
def add_product(
    line: str = Form(...),
    name: str = Form(...),
    db: Session = Depends(get_db),
):
    new_product = Product(line=line, name=name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)   # reload with DB-generated ID
    print("item added")
    return RedirectResponse(url="/", status_code=303)
    # return {"status": "success", "id": new_product.id}
