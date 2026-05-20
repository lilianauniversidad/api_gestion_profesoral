"""
rol.py - Modelos Pydantic para la tabla rol.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class RolBase(BaseModel):
    """Esquema base para rol."""
    nombre: str = Field(..., max_length=45)
    descripcion: Optional[str] = None
    activo: bool = True


class RolCreate(RolBase):
    """Esquema para crear rol."""
    pass


class RolUpdate(BaseModel):
    """Esquema para actualizar rol."""
    nombre: Optional[str] = Field(None, max_length=45)
    descripcion: Optional[str] = None
    activo: Optional[bool] = None


class RolResponse(RolBase):
    """Esquema de respuesta para rol."""
    id: int
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True