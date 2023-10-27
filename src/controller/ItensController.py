from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model.ItemModel import ItemModel

from repository.ItensRepository import persist_item
from service.ExcelService import read_sheet


app = FastAPI()

origins = [
    "*"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/item/")
async def save_item(item: ItemModel):
    try:
        persist_item(item)
        read_sheet(item.descricao)
        return {"message": "Item cadastrado com sucesso"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    

# @app.patch("/item/{id}")
# async def 