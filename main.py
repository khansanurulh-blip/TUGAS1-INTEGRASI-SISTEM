from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model data
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int 
    hobi: Optional[str] = None

# Simulasi database
data_mahasiswa = {}

# CREATE (POST)
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Mahasiswa):
    if item_id in data_mahasiswa:
        return {"error": "Data sudah ada"}
    data_mahasiswa[item_id] = item.dict()
    return {"message": "Data mahasiswa berhasil ditambahkan", "item": data_mahasiswa[item_id]}

# READ (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in data_mahasiswa:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    return {"item_id": item_id, 'item': data_mahasiswa[item_id]}

# UPDATE (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Mahasiswa):
    if item_id not in data_mahasiswa:
        return {"error": "Data mahasiswa tidak ditemukan"}
    data_mahasiswa[item_id] = item.dict()
    return {"message": "Data mahasiswa berhasil diperbarui", "item": data_mahasiswa[item_id]}

# DELETE (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in data_mahasiswa:
        return {"error": "Data mahasiswa tidak ditemukan"}
    deleted_item = data_mahasiswa.pop(item_id)
    return {"message": "Data mahasiswa berhasil dihapus", "deleted_item": deleted_item}