from sqlmodel import SQLModel, create_engine, Session
import os

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
cripta_db_dir = os.path.join(project_root_dir, 'Cripta')

# Asegura que el directorio Cripta existe
os.makedirs(cripta_db_dir, exist_ok=True)

# Construye la URL de la base de datos SQLite
DATABASE_URL = f"sqlite:///{os.path.join(cripta_db_dir, 'condenados.db')}"

# Crea el motor de la base de datos
# echo=True para ver las sentencias SQL generadas (útil para depuración)
engine = create_engine(DATABASE_URL, echo=True)

def crear_db_y_tablas():
    """
        Crea todas las tablas definidas en los modelos SQLModel en la base de datos.
        Debe llamarse una vez al inicio de la aplicación.
    """
    
    from BaseCondenados.cripta import Usuario
    SQLModel.metadata.create_all(engine)

def get_session():
    """
        Dependencia de FastAPI para obtener una sesión de base de datos.
        Asegura que la sesión se cierre correctamente después de la solicitud.
    """
    with Session(engine) as session:
        yield session
