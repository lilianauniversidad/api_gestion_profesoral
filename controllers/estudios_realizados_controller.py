"""
estudios_realizados_controller.py - Controlador para la tabla estudios_realizados.
"""
from fastapi import APIRouter, Query, HTTPException
from models.estudios_realizados import EstudiosRealizadosCreate, EstudiosRealizadosUpdate, EstudiosRealizadosResponse
from servicios.estudios_realizados_servicio import EstudiosRealizadosServicio

router = APIRouter(prefix="/api/estudios_realizados", tags=["estudios_realizados"])


@router.get("/", response_model=list[EstudiosRealizadosResponse])
async def listar_estudios(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los estudios_realizados."""
    servicio = EstudiosRealizadosServicio()
    estudios = await servicio.get_all(limite=limite)
    return estudios


@router.get("/{id}", response_model=EstudiosRealizadosResponse)
async def obtener_estudio(id: int, esquema: str = Query(default="public")):
    """Obtiene un estudios_realizados por id."""
    servicio = EstudiosRealizadosServicio()
    estudio = await servicio.get_by_id(id)
    
    if estudio is None:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    
    return estudio


@router.post("/", status_code=201, response_model=dict)
async def crear_estudio(estudio: EstudiosRealizadosCreate, esquema: str = Query(default="public")):
    """Crea un nuevo estudios_realizados."""
    servicio = EstudiosRealizadosServicio()
    exito = await servicio.create(estudio.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el estudio")
    
    return {"mensaje": "Estudio creado exitosamente", "id": estudio.id}


@router.put("/{id}", response_model=dict)
async def actualizar_estudio(id: int, estudio: EstudiosRealizadosUpdate, esquema: str = Query(default="public")):
    """Actualiza un estudios_realizados existente."""
    servicio = EstudiosRealizadosServicio()
    exito = await servicio.update(id, estudio.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    
    return {"mensaje": "Estudio actualizado exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_estudio(id: int, esquema: str = Query(default="public")):
    """Elimina un estudios_realizados por id."""
    servicio = EstudiosRealizadosServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    
    return None