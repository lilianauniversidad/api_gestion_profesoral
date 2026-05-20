"""
intereses_futuros_controller.py - Controlador para la tabla intereses_futuros.
"""
from fastapi import APIRouter, Query, HTTPException
from models.intereses_futuros import InteresesFuturosCreate, InteresesFuturosResponse
from servicios.intereses_futuros_servicio import InteresesFuturosServicio

router = APIRouter(prefix="/api/intereses_futuros", tags=["intereses_futuros"])


@router.get("/", response_model=list[InteresesFuturosResponse])
async def listar_intereses(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los registros de intereses_futuros."""
    servicio = InteresesFuturosServicio()
    registros = await servicio.get_all(limite=limite)
    return registros


@router.get("/{docente}/{termino_clave}", response_model=InteresesFuturosResponse)
async def obtener_interes(docente: int, termino_clave: str, esquema: str = Query(default="public")):
    """Obtiene un registro por PK compuesta."""
    servicio = InteresesFuturosServicio()
    registro = await servicio.get_by_id(docente, termino_clave)
    
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return registro


@router.post("/", status_code=201, response_model=dict)
async def crear_interes(registro: InteresesFuturosCreate, esquema: str = Query(default="public")):
    """Crea un nuevo registro en intereses_futuros."""
    servicio = InteresesFuturosServicio()
    exito = await servicio.create(registro.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el registro")
    
    return {"mensaje": "Registro creado exitosamente", "docente": registro.docente, "termino_clave": registro.termino_clave}


@router.delete("/{docente}/{termino_clave}", status_code=204)
async def eliminar_interes(docente: int, termino_clave: str, esquema: str = Query(default="public")):
    """Elimina un registro por PK compuesta."""
    servicio = InteresesFuturosServicio()
    exito = await servicio.delete(docente, termino_clave)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return None


@router.get("/docente/{docente}", response_model=list[InteresesFuturosResponse])
async def listar_por_docente(docente: int, esquema: str = Query(default="public")):
    """Lista todos los intereses de un docente."""
    servicio = InteresesFuturosServicio()
    registros = await servicio.get_by_docente(docente)
    return registros