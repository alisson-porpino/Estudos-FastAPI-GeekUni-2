from typing import Optional

from pydantic import BaseModel #as SCBaseModel



class CursoSchema(BaseModel): #SCBaseModel
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"id": {"alias": False}}
        