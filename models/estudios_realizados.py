"""
estudios_realizados.py - Modelos Pydantic para la tabla estudios_realizados.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class EstudiosRealizadosBase(BaseModel):
    """Esquema base para estudios_realizados."""
    titulo: str = Field(..., max_length=45)
    universidad: str = Field(..., max_length=50)
    fecha: date
    tipo: str = Field(..., max_length=45)
    ciudad: str = Field(..., max_length=45)
    docente: int
    ins_acreditada: int
    metodologia: str = Field(..., max_length=45)
    perfil_egresado: str
    pais: str = Field(..., max_length=45)


class EstudiosRealizadosCreate(EstudiosRealizadosBase):
    """Esquema para crear estudios_realizados."""
    id: int


class EstudiosRealizadosUpdate(BaseModel):
    """Esquema para actualizar estudios_realizados."""
    titulo: Optional[str] = Field(None, max_length=45)
    universidad: Optional[str] = Field(None, max_length=50)
    fecha: Optional[date] = None
    tipo: Optional[str] = Field(None, max_length=45)
    ciudad: Optional[str] = Field(None, max_length=45)
    docente: Optional[int] = None
    ins_acreditada: Optional[int] = None
    metodologia: Optional[str] = Field(None, max_length=45)
    perfil_egresado: Optional[str] = None
    pais: Optional[str] = Field(None, max_length=45)


class EstudiosRealizadosResponse(EstudiosRealizadosBase):
    """Esquema de respuesta para estudios_realizados."""
    id: int
    
    class Config:
        from_attributes = True