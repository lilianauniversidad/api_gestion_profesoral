"""
usuario_controller.py - Controlador para la tabla usuario.
"""
from fastapi import APIRouter, Query, HTTPException
from models.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from servicios.usuario_servicio import UsuarioServicio

router = APIRouter(prefix="/api/usuario", tags=["usuario"])


@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los usuarios."""
    servicio = UsuarioServicio()
    usuarios = await servicio.get_all(limite=limite)
    return usuarios


@router.get("/{id}", response_model=UsuarioResponse)
async def obtener_usuario(id: int, esquema: str = Query(default="public")):
    """Obtiene un usuario por id."""
    servicio = UsuarioServicio()
    usuario = await servicio.get_by_id(id)
    
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario


@router.post("/", status_code=201, response_model=dict)
async def crear_usuario(usuario: UsuarioCreate, esquema: str = Query(default="public")):
    """Crea un nuevo usuario."""
    servicio = UsuarioServicio()
    
    # Verificar si el username ya existe
    existente = await servicio.get_by_username(usuario.username)
    if existente:
        raise HTTPException(status_code=400, detail="El username ya está registrado")
    
    exito = await servicio.create(usuario.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el usuario")
    
    return {"mensaje": "Usuario creado exitosamente"}


@router.put("/{id}", response_model=dict)
async def actualizar_usuario(id: int, usuario: UsuarioUpdate, esquema: str = Query(default="public")):
    """Actualiza un usuario existente."""
    servicio = UsuarioServicio()
    exito = await servicio.update(id, usuario.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return {"mensaje": "Usuario actualizado exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_usuario(id: int, esquema: str = Query(default="public")):
    """Elimina un usuario por id."""
    servicio = UsuarioServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return None