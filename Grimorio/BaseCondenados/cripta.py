# Este archivo contiene el router de FastAPI para usuarios,
# los modelos SQLModel y Pydantic, y la lógica de autenticación.

import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, SQLModel, Field
from passlib.context import CryptContext
from pydantic import BaseModel

# Importa la función get_session desde baseDatos.py
from BaseCondenados.baseDatos import get_session

# Modelo SQLModel
class Usuario(SQLModel, table=True):
    """
        Modelo SQLModel para la tabla de usuarios.
        Define la estructura de la tabla 'usuario' en la base de datos.
    """
    __tablename__ = "usuario" # Nombre de la tabla en la base de datos

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    nombreUsuario: str = Field(nullable=False)

    # Nuevos campos opcionales sugeridos
    bio: Optional[str] = Field(default=None, max_length=500)
    timezone: Optional[str] = Field(default=None, max_length=50)
    lenguaje: Optional[str] = Field(default=None, max_length=10)
    
    # Campos para la integración con partidas (jugador/narrador)
    # NOTA: La lógica para asignar estos roles y partida_id
    # debería residir en las rutas de la API relacionadas con las partidas.
    rol_partida: Optional[str] = Field(default=None, max_length=20) # 'jugador' o 'narrador'
    partida_id: Optional[uuid.UUID] = Field(default=None, index=True) # ID de la partida actual

    fecha_creacion: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    fecha_actualizacion: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

# Schemas Pydantic
class UsuarioRegistro(BaseModel):
    """
        Schema para el registro de un nuevo usuario.
    """
    email: str
    password: str
    nombreUsuario: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    timezone: Optional[str] = None
    lenguaje: Optional[str] = None

class UsuarioInicio(BaseModel):
    """
        Schema para el inicio de sesión de un usuario.
    """
    email: str
    password: str
    
class UsuarioActualizar(BaseModel):
    """
        Schema para la actualización de datos de un usuario.
        Todos los campos son opcionales para permitir actualizaciones parciales.
    """
    nombreUsuario: Optional[str] = None
    password: Optional[str] = None # Para cambiar la contraseña
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    timezone: Optional[str] = None
    lenguaje: Optional[str] = None
    # No se permite actualizar rol_partida o partida_id directamente aquí,
    # ya que su gestión debería ser a través de las rutas de partida.
class UsuarioRespuesta(BaseModel):
    """
        Schema para la respuesta de un usuario, excluyendo el hash de la contraseña.
    """
    id: uuid.UUID
    email: str
    nombreUsuario: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    timezone: Optional[str] = None
    lenguaje: Optional[str] = None
    rol_partida: Optional[str] = None
    partida_id: Optional[uuid.UUID] = None
    fecha_creacion: datetime
    fecha_actualizacion: datetime

# Lógica de Hashing de Contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Router de FastAPI para Usuarios
router = APIRouter(
    prefix="/cripta",  # Prefijo para todas las rutas en este router
    tags=["Usuarios"], # Etiqueta para la documentación de Swagger UI
)


@router.post("/registro", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar_usuario(u: UsuarioRegistro, session: Session = Depends(get_session)):
    """
        Registra un nuevo usuario en el sistema.
    """
    # Verifica si el email ya está registrado
    existente = session.exec(select(Usuario).where(Usuario.email == u.email)).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ya registrado")

    # Crea un nuevo usuario con la contraseña hasheada y los nuevos campos
    nuevo = Usuario(
        email=u.email,
        nombreUsuario=u.nombreUsuario,
        avatar_url=u.avatar_url,
        bio=u.bio,
        timezone=u.timezone,
        lenguaje=u.lenguaje,
        password_hash=pwd_context.hash(u.password)
    )
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo) # Actualiza el objeto para obtener el ID y fechas generadas
    return nuevo

@router.post("/inicio", response_model=UsuarioRespuesta)
def iniciar_sesion(data: UsuarioInicio, session: Session = Depends(get_session)):
    """
        Inicia sesión de un usuario y devuelve sus datos.
    """
    usuario = session.exec(select(Usuario).where(Usuario.email == data.email)).first()
    if not usuario or not pwd_context.verify(data.password, usuario.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return usuario

@router.get("/{usuario_id}", response_model=UsuarioRespuesta)
def obtener_usuario(usuario_id: uuid.UUID, session: Session = Depends(get_session)):
    """
        Obtiene los datos de un usuario por su ID.
    """
    usuario = session.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioRespuesta)
def actualizar_usuario(
    usuario_id: uuid.UUID,
    u_update: UsuarioActualizar,
    session: Session = Depends(get_session)
):
    """
        Actualiza los datos de un usuario existente.
        Permite actualizaciones parciales (PATCH-like) si los campos son opcionales.
    """
    usuario = session.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    # Actualiza solo los campos que se proporcionaron en la solicitud
    update_data = u_update.model_dump(exclude_unset=True) # Usa model_dump para Pydantic v2+
    
    # Manejo especial para la contraseña si se está actualizando
    if "password" in update_data:
        update_data["password_hash"] = pwd_context.hash(update_data.pop("password"))

    # Aplica las actualizaciones al modelo de SQLAlchemy
    for key, value in update_data.items():
        setattr(usuario, key, value)
    
    session.add(usuario) # Añade el objeto actualizado a la sesión (para que SQLModel lo rastree)
    session.commit()
    session.refresh(usuario) # Refresca el objeto para obtener los datos actualizados de la DB
    return usuario

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: uuid.UUID, session: Session = Depends(get_session)):
    """
        Elimina un usuario por su ID.
    """
    usuario = session.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    session.delete(usuario)
    session.commit()
    return {"message": "Usuario eliminado exitosamente"}