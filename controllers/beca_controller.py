"""
beca_controller.py - Controlador para la tabla beca.
"""
from fastapi import APIRouter, Query, HTTPException
from models.beca import BecaCreate, BecaUpdate, BecaResponse
from servicios.beca_servicio import BecaServicio

router = APIRouter(prefix="/api/beca", tags=["beca"])


@router.get("/", response_model=list[BecaResponse])
async def listar_becas(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todas las becas."""
    servicio = BecaServicio()
    becas = await servicio.get_all(limite=limite)
    return becas


@router.get("/{estudios}", response_model=BecaResponse)
async def obtener_beca(estudios: int, esquema: str = Query(default="public")):
    """Obtiene una beca por id de estudio."""
    servicio = BecaServicio()
    beca = await servicio.get_by_id(estudios)
    
    if beca is None:
        raise HTTPException(status_code=404, detail="Beca no encontrada")
    
    return beca


@router.post("/", status_code=201, response_model=dict)
async def crear_beca(beca: BecaCreate, esquema: str = Query(default="public")):
    """Crea una nueva beca."""
    servicio = BecaServicio()
    exito = await servicio.create(beca.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear la beca")
    
    return {"mensaje": "Beca creada exitosamente", "estudios": beca.estudios}


@router.put("/{estudios}", response_model=dict)
async def actualizar_beca(estudios: int, beca: BecaUpdate, esquema: str = Query(default="public")):
    """Actualiza una beca existente."""
    servicio = BecaServicio()
    exito = await servicio.update(estudios, beca.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Beca no encontrada")
    
    return {"mensaje": "Beca actualizada exitosamente"}


@router.delete("/{estudios}", status_code=204)
async def eliminar_beca(estudios: int, esquema: str = Query(default="public")):
    """Elimina una beca por id de estudio."""
    servicio = BecaServicio()
    exito = await servicio.delete(estudios)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Beca no encontrada")
    
    return None