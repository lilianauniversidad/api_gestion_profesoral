"""
rol_controller.py - Controlador para la tabla rol.
"""
from fastapi import APIRouter, Query, HTTPException
from models.rol import RolCreate, RolUpdate, RolResponse
from servicios.rol_servicio import RolServicio

router = APIRouter(prefix="/api/rol", tags=["rol"])


@router.get("/", response_model=list[RolResponse])
async def listar_roles(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los roles."""
    servicio = RolServicio()
    roles = await servicio.get_all(limite=limite)
    return roles


@router.get("/{id}", response_model=RolResponse)
async def obtener_rol(id: int, esquema: str = Query(default="public")):
    """Obtiene un rol por id."""
    servicio = RolServicio()
    rol = await servicio.get_by_id(id)
    
    if rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    return rol


@router.post("/", status_code=201, response_model=dict)
async def crear_rol(rol: RolCreate, esquema: str = Query(default="public")):
    """Crea un nuevo rol."""
    servicio = RolServicio()
    exito = await servicio.create(rol.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el rol")
    
    return {"mensaje": "Rol creado exitosamente"}


@router.put("/{id}", response_model=dict)
async def actualizar_rol(id: int, rol: RolUpdate, esquema: str = Query(default="public")):
    """Actualiza un rol existente."""
    servicio = RolServicio()
    exito = await servicio.update(id, rol.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    return {"mensaje": "Rol actualizado exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_rol(id: int, esquema: str = Query(default="public")):
    """Elimina un rol por id."""
    servicio = RolServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    return None