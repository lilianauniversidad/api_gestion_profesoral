"""
beca_repositorio.py - Repositorio para la tabla beca.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class BecaRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de beca."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "beca"
        self._pk = "estudios"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todas las becas."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY {self._pk} ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, estudios: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene una beca por id de estudio."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE {self._pk} = :estudios"
        resultados = await self._ejecutar_query(query, {"estudios": estudios})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea una nueva beca."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, estudios: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza una beca existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE {self._pk} = :estudios"
        datos["estudios"] = estudios
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, estudios: int, esquema: str = "public") -> bool:
        """Elimina una beca por id de estudio."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE {self._pk} = :estudios"
        filas = await self._ejecutar_comando(query, {"estudios": estudios})
        return filas > 0