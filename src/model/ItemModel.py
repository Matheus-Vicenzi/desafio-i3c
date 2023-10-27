from typing import Union
from pydantic import BaseModel

class ItemModel(BaseModel):
    id: Union[int, None] = None
    descricao: str
    quantidade: int
    valor: float
    valor_36_meses: float
    valor_60_meses: float
