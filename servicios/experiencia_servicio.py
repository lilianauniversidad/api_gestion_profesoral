"""
experiencia_servicio.py - Servicio para la tabla experiencia.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.experiencia_repositorio import ExperienciaRepositorio


class ExperienciaServicio:
    """Servicio para operaciones de negocio de experiencia."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = ExperienciaRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todas las experiencias."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene una experiencia por id."""
        return await self._repo.obtener_por_id(id)
    
    async def create(self, datos: dict) -> bool:
        """Crea una nueva experiencia."""
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza una experiencia."""
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina una experiencia."""
        return await self._repo.eliminar(id)
    
    async def get_by_docente(self, docente: int) -> list[dict]:
        """Obtiene todas las experiencias de un docente."""
        return await self._repo.obtener_por_docente(docente)