"""
estudios_realizados_servicio.py - Servicio para la tabla estudios_realizados.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.estudios_realizados_repositorio import EstudiosRealizadosRepositorio


class EstudiosRealizadosServicio:
    """Servicio para operaciones de negocio de estudios_realizados."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = EstudiosRealizadosRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los estudios_realizados."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene un estudios_realizados por id."""
        return await self._repo.obtener_por_id(id)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo estudios_realizados."""
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza un estudios_realizados."""
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina un estudios_realizados."""
        return await self._repo.eliminar(id)