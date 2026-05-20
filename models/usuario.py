"""
usuario.py - Modelos Pydantic para la tabla usuario.
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    """Esquema base para usuario."""
    username: str = Field(..., max_length=45)
    email: EmailStr
    nombre_completo: str = Field(..., max_length=100)
    activo: bool = True


class UsuarioCreate(UsuarioBase):
    """Esquema para crear usuario."""
    password: str = Field(..., min_length=6)


class UsuarioUpdate(BaseModel):
    """Esquema para actualizar usuario."""
    username: Optional[str] = Field(None, max_length=45)
    email: Optional[EmailStr] = None
    nombre_completo: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=6)
    activo: Optional[bool] = None


class UsuarioResponse(UsuarioBase):
    """Esquema de respuesta para usuario."""
    id: int
    fecha_creacion: datetime
    ultimo_acceso: Optional[datetime] = None
    
    class Config:
        from_attributes = True