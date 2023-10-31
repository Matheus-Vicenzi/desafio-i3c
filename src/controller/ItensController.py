from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model.ItemModel import ItemModel

from repository.ItensRepository import save_item as save_item_db
from repository.ItensRepository import change_item as change_item_db
from repository.ItensRepository import get_item as get_item_db

from service.ExcelService import change_item as change_item_excel
from service.ExcelService import change_item_total_value


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
        save_item_db(item)
        return {"message": "Item cadastrado com sucesso",
                "content": item}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.patch("/item/{id}")
async def change_price_quantity(id: int, new_price_value: float, new_quantity_value: int):
    try:
        change_item_db(id, float(new_price_value), int(new_quantity_value))
        item: ItemModel = get_item_db(id)
        # total_item_price = change_item_excel(id, float(new_price_value), int(new_quantity_value))
        return {"message": "Preço alterado com sucesso",
                "content": {"newTotalPrice": item.valor * item.quantidade}
                }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
