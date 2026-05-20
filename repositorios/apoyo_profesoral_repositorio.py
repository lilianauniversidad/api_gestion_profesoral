"""
apoyo_profesoral_repositorio.py - Repositorio para la tabla apoyo_profesoral.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class ApoyoProfesoralRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de apoyo_profesoral."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "apoyo_profesoral"
        self._pk = "estudios"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los apoyos profesorales."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY {self._pk} ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, estudios: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un apoyo por id de estudio."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE {self._pk} = :estudios"
        resultados = await self._ejecutar_query(query, {"estudios": estudios})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo apoyo profesoral."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, estudios: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un apoyo profesoral existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE {self._pk} = :estudios"
        datos["estudios"] = estudios
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, estudios: int, esquema: str = "public") -> bool:
        """Elimina un apoyo profesoral por id de estudio."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE {self._pk} = :estudios"
        filas = await self._ejecutar_comando(query, {"estudios": estudios})
        return filas > 0