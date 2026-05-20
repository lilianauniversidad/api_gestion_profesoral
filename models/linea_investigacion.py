"""
models/linea_investigacion.py — Modelo Pydantic para linea_investigacion.
Tabla: linea_investigacion (id SERIAL, nombre, descripcion)
"""
from pydantic import BaseModel, Field, ConfigDict


class LineaInvestigacionBase(BaseModel):
    """Campos base compartidos para crear y actualizar."""
    nombre: str = Field(..., max_length=45, description="Nombre de la línea de investigación")
    descripcion: str = Field(..., max_length=256, description="Descripción de la línea")


class LineaInvestigacionCreate(LineaInvestigacionBase):
    """Modelo para crear una nueva línea de investigación."""
    pass


class LineaInvestigacionUpdate(BaseModel):
    """Modelo para actualizar una línea de investigación."""
    nombre: str | None = Field(None, max_length=45)
    descripcion: str | None = Field(None, max_length=256)


class LineaInvestigacion(LineaInvestigacionBase):
    """Modelo completo para respuestas de la API."""
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="ID de la línea de investigación (autoincremental)")