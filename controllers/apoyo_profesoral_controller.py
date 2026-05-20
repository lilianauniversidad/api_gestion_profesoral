"""
apoyo_profesoral_controller.py - Controlador para la tabla apoyo_profesoral.
"""
from fastapi import APIRouter, Query, HTTPException
from models.apoyo_profesoral import ApoyoProfesoralCreate, ApoyoProfesoralUpdate, ApoyoProfesoralResponse
from servicios.apoyo_profesoral_servicio import ApoyoProfesoralServicio

router = APIRouter(prefix="/api/apoyo_profesoral", tags=["apoyo_profesoral"])


@router.get("/", response_model=list[ApoyoProfesoralResponse])
async def listar_apoyos(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los apoyos profesorales."""
    servicio = ApoyoProfesoralServicio()
    apoyos = await servicio.get_all(limite=limite)
    return apoyos


@router.get("/{estudios}", response_model=ApoyoProfesoralResponse)
async def obtener_apoyo(estudios: int, esquema: str = Query(default="public")):
    """Obtiene un apoyo por id de estudio."""
    servicio = ApoyoProfesoralServicio()
    apoyo = await servicio.get_by_id(estudios)
    
    if apoyo is None:
        raise HTTPException(status_code=404, detail="Apoyo no encontrado")
    
    return apoyo


@router.post("/", status_code=201, response_model=dict)
async def crear_apoyo(apoyo: ApoyoProfesoralCreate, esquema: str = Query(default="public")):
    """Crea un nuevo apoyo profesoral."""
    servicio = ApoyoProfesoralServicio()
    exito = await servicio.create(apoyo.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el apoyo")
    
    return {"mensaje": "Apoyo creado exitosamente", "estudios": apoyo.estudios}


@router.put("/{estudios}", response_model=dict)
async def actualizar_apoyo(estudios: int, apoyo: ApoyoProfesoralUpdate, esquema: str = Query(default="public")):
    """Actualiza un apoyo profesoral existente."""
    servicio = ApoyoProfesoralServicio()
    exito = await servicio.update(estudios, apoyo.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Apoyo no encontrado")
    
    return {"mensaje": "Apoyo actualizado exitosamente"}


@router.delete("/{estudios}", status_code=204)
async def eliminar_apoyo(estudios: int, esquema: str = Query(default="public")):
    """Elimina un apoyo profesoral por id de estudio."""
    servicio = ApoyoProfesoralServicio()
    exito = await servicio.delete(estudios)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Apoyo no encontrado")
    
    return None