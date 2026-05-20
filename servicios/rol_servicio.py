"""
rol_servicio.py - Servicio para la tabla rol.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.rol_repositorio import RolRepositorio


class RolServicio:
    """Servicio para operaciones de negocio de rol."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = RolRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los roles."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene un rol por id."""
        return await self._repo.obtener_por_id(id)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo rol."""
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza un rol."""
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina un rol."""
        return await self._repo.eliminar(id)