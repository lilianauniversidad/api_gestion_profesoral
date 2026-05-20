"""
usuario_servicio.py - Servicio para la tabla usuario.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.usuario_repositorio import UsuarioRepositorio
from passlib.context import CryptContext


class UsuarioServicio:
    """Servicio para operaciones de negocio de usuario."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = UsuarioRepositorio(proveedor.obtener_cadena_conexion())
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los usuarios."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene un usuario por id."""
        return await self._repo.obtener_por_id(id)
    
    async def get_by_username(self, username: str) -> Optional[dict]:
        """Obtiene un usuario por username."""
        return await self._repo.obtener_por_username(username)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo usuario con password hasheado."""
        datos["password"] = self._pwd_context.hash(datos["password"])
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza un usuario."""
        if "password" in datos and datos["password"]:
            datos["password"] = self._pwd_context.hash(datos["password"])
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina un usuario."""
        return await self._repo.eliminar(id)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verifica si la contraseña coincide con el hash."""
        return self._pwd_context.verify(plain_password, hashed_password)