"""
apoyo_profesoral_servicio.py - Servicio para la tabla apoyo_profesoral.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.apoyo_profesoral_repositorio import ApoyoProfesoralRepositorio


class ApoyoProfesoralServicio:
    """Servicio para operaciones de negocio de apoyo_profesoral."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = ApoyoProfesoralRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los apoyos profesorales."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, estudios: int) -> Optional[dict]:
        """Obtiene un apoyo por id de estudio."""
        return await self._repo.obtener_por_id(estudios)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo apoyo profesoral."""
        return await self._repo.crear(datos)
    
    async def update(self, estudios: int, datos: dict) -> bool:
        """Actualiza un apoyo profesoral."""
        return await self._repo.actualizar(estudios, datos)
    
    async def delete(self, estudios: int) -> bool:
        """Elimina un apoyo profesoral."""
        return await self._repo.eliminar(estudios)