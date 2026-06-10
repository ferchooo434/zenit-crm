from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

Base = declarative_base()

# ── PROSPECTOS ──────────────────────────────────────────
class Prospecto(Base):
    __tablename__ = "prospectos"

    id               = Column(Integer, primary_key=True)
    empresa          = Column(String, nullable=False)
    contacto         = Column(String)
    telefono         = Column(String)
    email            = Column(String)
    whatsapp         = Column(String)
    instagram        = Column(String)
    facebook         = Column(String)
    sector           = Column(String)
    ubicacion        = Column(String)
    estado_pipeline  = Column(String, default="Prospecto")
    fecha_registro   = Column(Date, default=date.today)

    diagnosticos  = relationship("Diagnostico",  back_populates="prospecto", cascade="all, delete")
    seguimientos  = relationship("Seguimiento",  back_populates="prospecto", cascade="all, delete")
    reuniones     = relationship("Reunion",      back_populates="prospecto", cascade="all, delete")
    propuestas    = relationship("Propuesta",    back_populates="prospecto", cascade="all, delete")
    clientes      = relationship("Cliente",      back_populates="prospecto", cascade="all, delete")

# ── DIAGNÓSTICO COMERCIAL ────────────────────────────────
class Diagnostico(Base):
    __tablename__ = "diagnosticos"

    id             = Column(Integer, primary_key=True)
    prospecto_id   = Column(Integer, ForeignKey("prospectos.id"))
    branding       = Column(Integer, default=0)
    redes_sociales = Column(Integer, default=0)
    comunicacion   = Column(Integer, default=0)
    contenido      = Column(Integer, default=0)
    publicidad     = Column(Integer, default=0)
    observaciones  = Column(Text)

    prospecto = relationship("Prospecto", back_populates="diagnosticos")

# ── SEGUIMIENTOS ─────────────────────────────────────────
class Seguimiento(Base):
    __tablename__ = "seguimientos"

    id             = Column(Integer, primary_key=True)
    prospecto_id   = Column(Integer, ForeignKey("prospectos.id"))
    fecha_proxima  = Column(Date)
    canal          = Column(String)
    comentario     = Column(Text)
    completado     = Column(Boolean, default=False)

    prospecto = relationship("Prospecto", back_populates="seguimientos")

# ── REUNIONES ────────────────────────────────────────────
class Reunion(Base):
    __tablename__ = "reuniones"

    id            = Column(Integer, primary_key=True)
    prospecto_id  = Column(Integer, ForeignKey("prospectos.id"))
    fecha         = Column(Date)
    resultado     = Column(Text)
    proximo_paso  = Column(Text)

    prospecto = relationship("Prospecto", back_populates="reuniones")

# ── PROPUESTAS ───────────────────────────────────────────
class Propuesta(Base):
    __tablename__ = "propuestas"

    id            = Column(Integer, primary_key=True)
    prospecto_id  = Column(Integer, ForeignKey("prospectos.id"))
    servicio      = Column(String)
    monto         = Column(Float, default=0)
    fecha_envio   = Column(Date)
    estado        = Column(String, default="En preparación")

    prospecto = relationship("Prospecto", back_populates="propuestas")

# ── CLIENTES ─────────────────────────────────────────────
class Cliente(Base):
    __tablename__ = "clientes"

    id                  = Column(Integer, primary_key=True)
    prospecto_id        = Column(Integer, ForeignKey("prospectos.id"))
    fecha_inicio        = Column(Date, default=date.today)
    servicio_contratado = Column(String)
    fee_mensual         = Column(Float, default=0)
    estado              = Column(String, default="Activo")

    prospecto = relationship("Prospecto", back_populates="clientes")

# ── CONEXIÓN ─────────────────────────────────────────────
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "zenit_crm.db")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()