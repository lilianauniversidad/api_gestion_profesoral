"""
linea_investigacion_controller.py — Controller para línea de investigación.
"""
from fastapi import APIRouter, HTTPException, Query
from servicios.fabrica_servicios import crear_servicio_linea_investigacion
from models.linea_investigacion import LineaInvestigacion, LineaInvestigacionCreate, LineaInvestigacionUpdate

router = APIRouter(prefix="/api/linea_investigacion", tags=["Línea Investigación"])


@router.get("/", response_model=list[LineaInvestigacion])
async def listar_linea_investigacion(
    esquema: str = Query(default="public"),
    limite: int = Query(default=1000, ge=1, le=10000)
):
    servicio = crear_servicio_linea_investigacion()
    try:
        return await servicio.listar(limite=limite)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=LineaInvestigacion)
async def obtener_linea_investigacion(id: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_linea_investigacion()
    resultado = await servicio.obtener(id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Línea de investigación no encontrada")
    return resultado


@router.post("/", response_model=LineaInvestigacion, status_code=201)
async def crear_linea_investigacion(datos: LineaInvestigacionCreate, esquema: str = Query(default="public")):
    servicio = crear_servicio_linea_investigacion()
    resultado = await servicio.crear(datos.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="No se pudo crear la línea de investigación")
    return resultado


@router.put("/{id}", response_model=LineaInvestigacion)
async def actualizar_linea_investigacion(id: int, datos: LineaInvestigacionUpdate, esquema: str = Query(default="public")):
    servicio = crear_servicio_linea_investigacion()
    datos_dict = {k: v for k, v in datos.model_dump().items() if v is not None}
    resultado = await servicio.actualizar(id, datos_dict)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Línea de investigación no encontrada")
    return resultado


@router.delete("/{id}", status_code=204)
async def eliminar_linea_investigacion(id: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_linea_investigacion()
    exito = await servicio.eliminar(id)
    if not exito:
        raise HTTPException(status_code=404, detail="Línea de investigación no encontrada")
    return None
