"""
beca.py - Modelos Pydantic para la tabla beca.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class BecaBase(BaseModel):
    """Esquema base para beca."""
    tipo: str = Field(..., max_length=45)
    institucion: str = Field(..., max_length=45)
    fecha_inicio: date
    fecha_fin: Optional[date] = None


class BecaCreate(BecaBase):
    """Esquema para crear beca."""
    estudios: int


class BecaUpdate(BaseModel):
    """Esquema para actualizar beca."""
    tipo: Optional[str] = Field(None, max_length=45)
    institucion: Optional[str] = Field(None, max_length=45)
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None


class BecaResponse(BecaBase):
    """Esquema de respuesta para beca."""
    estudios: int
    
    class Config:
        from_attributes = True