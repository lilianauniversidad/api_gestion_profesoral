"""
intereses_futuros_repositorio.py - Repositorio para la tabla intereses_futuros.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class InteresesFuturosRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de intereses_futuros."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "intereses_futuros"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de intereses_futuros."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY docente, termino_clave ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, docente: int, termino_clave: str, esquema: str = "public") -> Optional[dict]:
        """Obtiene un registro por PK compuesta (docente, termino_clave)."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE docente = :docente AND termino_clave = :termino_clave"
        resultados = await self._ejecutar_query(query, {"docente": docente, "termino_clave": termino_clave})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro en intereses_futuros."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, docente: int, termino_clave: str, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente (no aplica para esta tabla)."""
        return False
    
    async def eliminar(self, docente: int, termino_clave: str, esquema: str = "public") -> bool:
        """Elimina un registro por PK compuesta."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE docente = :docente AND termino_clave = :termino_clave"
        filas = await self._ejecutar_comando(query, {"docente": docente, "termino_clave": termino_clave})
        return filas > 0
    
    async def obtener_por_docente(self, docente: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los intereses de un docente."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE docente = :docente ORDER BY termino_clave ASC"
        return await self._ejecutar_query(query, {"docente": docente})