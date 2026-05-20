"""
beca_servicio.py - Servicio para la tabla beca.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.beca_repositorio import BecaRepositorio


class BecaServicio:
    """Servicio para operaciones de negocio de beca."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = BecaRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todas las becas."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, estudios: int) -> Optional[dict]:
        """Obtiene una beca por id de estudio."""
        return await self._repo.obtener_por_id(estudios)
    
    async def create(self, datos: dict) -> bool:
        """Crea una nueva beca."""
        return await self._repo.crear(datos)
    
    async def update(self, estudios: int, datos: dict) -> bool:
        """Actualiza una beca."""
        return await self._repo.actualizar(estudios, datos)
    
    async def delete(self, estudios: int) -> bool:
        """Elimina una beca."""
        return await self._repo.eliminar(estudios)