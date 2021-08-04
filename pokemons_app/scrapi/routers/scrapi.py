from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from scrapi import schemas
from sqlalchemy.orm import Session
from scrapi.repository import scrapi as sc
import os
from fastapi.responses import FileResponse
router = APIRouter(
    prefix="/scrapi",
    tags=['Scrapis']
)


print(os.path.dirname(os.getcwd()))
path=os.path.dirname(os.getcwd())

@router.get('/test', responses={200: {"description": "A scrpy web.", "content" : {"application/vnd..." : {"example" : "No example available."}}}})
def download_products(name: str):
    sc.products(name)
    file_path = os.path.join(path, f"pokemons_app\\scrapi\\{name}.xlsx")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=f"{name}.xlsx")
    return {"error" : "File not found!"}
    