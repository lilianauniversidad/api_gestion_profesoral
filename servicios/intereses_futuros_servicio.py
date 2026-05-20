"""
intereses_futuros_servicio.py - Servicio para la tabla intereses_futuros.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.intereses_futuros_repositorio import InteresesFuturosRepositorio


class InteresesFuturosServicio:
    """Servicio para operaciones de negocio de intereses_futuros."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = InteresesFuturosRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, docente: int, termino_clave: str) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        return await self._repo.obtener_por_id(docente, termino_clave)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo registro."""
        return await self._repo.crear(datos)
    
    async def update(self, docente: int, termino_clave: str, datos: dict) -> bool:
        """Actualiza un registro (no aplica)."""
        return await self._repo.actualizar(docente, termino_clave, datos)
    
    async def delete(self, docente: int, termino_clave: str) -> bool:
        """Elimina un registro."""
        return await self._repo.eliminar(docente, termino_clave)
    
    async def get_by_docente(self, docente: int) -> list[dict]:
        """Obtiene todos los intereses de un docente."""
        return await self._repo.obtener_por_docente(docente)