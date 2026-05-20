"""
experiencia_controller.py - Controlador para la tabla experiencia.
"""
from fastapi import APIRouter, Query, HTTPException
from models.experiencia import ExperienciaCreate, ExperienciaUpdate, ExperienciaResponse
from servicios.experiencia_servicio import ExperienciaServicio

router = APIRouter(prefix="/api/experiencia", tags=["experiencia"])


@router.get("/", response_model=list[ExperienciaResponse])
async def listar_experiencias(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todas las experiencias laborales de docentes."""
    servicio = ExperienciaServicio()
    experiencias = await servicio.get_all(limite=limite)
    return experiencias


@router.get("/{id}", response_model=ExperienciaResponse)
async def obtener_experiencia(id: int, esquema: str = Query(default="public")):
    """Obtiene una experiencia por id."""
    servicio = ExperienciaServicio()
    experiencia = await servicio.get_by_id(id)
    
    if experiencia is None:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    
    return experiencia


@router.post("/", status_code=201, response_model=dict)
async def crear_experiencia(experiencia: ExperienciaCreate, esquema: str = Query(default="public")):
    """Crea una nueva experiencia laboral de docente."""
    servicio = ExperienciaServicio()
    exito = await servicio.create(experiencia.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear la experiencia")
    
    return {"mensaje": "Experiencia creada exitosamente", "id": experiencia.docente}


@router.put("/{id}", response_model=dict)
async def actualizar_experiencia(id: int, experiencia: ExperienciaUpdate, esquema: str = Query(default="public")):
    """Actualiza una experiencia existente."""
    servicio = ExperienciaServicio()
    exito = await servicio.update(id, experiencia.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    
    return {"mensaje": "Experiencia actualizada exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_experiencia(id: int, esquema: str = Query(default="public")):
    """Elimina una experiencia por id."""
    servicio = ExperienciaServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    
    return None


@router.get("/docente/{docente}", response_model=list[ExperienciaResponse])
async def listar_por_docente(docente: int, esquema: str = Query(default="public")):
    """Lista todas las experiencias de un docente."""
    servicio = ExperienciaServicio()
    experiencias = await servicio.get_by_docente(docente)
    return experiencias