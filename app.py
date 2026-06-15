import streamlit as st
from database import init_db, get_session, Prospecto, Seguimiento, Reunion, Propuesta, Cliente
from datetime import date

init_db()

# ── USUARIOS ─────────────────────────────────────────────

USUARIOS = {
    "Fnavarro": {
        "password": "zenit002",
        "rol": "admin",
        "nombre": "Fernando Navarro"
    },

    "Lurista": {
        "password": "zenit001",
        "rol": "SEO",
        "nombre": "Luis Urista"
    },

    "Larias": {
        "password": "zenit003",
        "rol": "Directora de Estrategias",
        "nombre": "Lizbeth Hernandez"
    }
}

# ── LOGIN ────────────────────────────────────────────────

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = ""
    
if "nombre" not in st.session_state:
    st.session_state.nombre = ""

if "rol" not in st.session_state:
    st.session_state.rol = ""

if not st.session_state.autenticado:

    st.markdown("""
<style>
.block-container {
    max-width: 420px;
    margin: auto;
    padding-top: 8rem;
}

[data-testid="stToolbar"] {
    visibility: hidden !important;
}

[data-testid="stHeader"] {
    visibility: visible !important;
    height: auto !important;
}

header {
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center;margin-bottom:2rem;'>
        <div style='font-size:2.5rem;font-weight:800;line-height:1;'>
            zenit <span style='color:#39FF14'>CRM</span>
        </div>
        <div style='color:#ffffff;font-size:0.7rem;letter-spacing:0.15em;margin-top:4px;'>
            MARKETING & BRANDING
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("login"):

        usuario = st.text_input("Usuario")

        contrasena = st.text_input(
            "Contraseña",
            type="password"
        )

        entrar = st.form_submit_button(
            "Entrar",
            use_container_width=True
        )

        if entrar:

            if (
                usuario in USUARIOS
                and USUARIOS[usuario]["password"] == contrasena
            ):

                st.session_state.autenticado = True
                st.session_state.usuario = usuario
                st.session_state.rol = USUARIOS[usuario]["rol"]
                st.session_state.nombre = USUARIOS[usuario]["nombre"]

                st.rerun()

            else:
                st.error("Usuario o contraseña incorrectos.")

    st.stop()

    st.markdown("""
    <div style='text-align:center;margin-bottom:2rem;'>
        <div style='font-size:2.5rem;font-weight:800;line-height:1;'>
            zenit <span style='color:#39FF14'>CRM</span>
        </div>
        <div style='color:#ffffff;font-size:0.7rem;letter-spacing:0.15em;margin-top:4px;'>
            MARKETING & BRANDING
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("login"):
        usuario    = st.text_input("Usuario")
        contrasena = st.text_input("Contraseña", type="password")
        entrar     = st.form_submit_button("Entrar", use_container_width=True)

        if entrar:
            if usuario in USUARIOS and USUARIOS[usuario]["password"] == contrasena:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario
                st.session_state.rol = USUARIOS[usuario]["rol"]
                st.session_state.nombre = USUARIOS[usuario]["nombre"]
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

    st.stop()

st.set_page_config(
    page_title="ZENIT CRM",
    layout="wide",
    initial_sidebar_state="expanded"
)

    
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

[data-testid="stSidebar"] {
    background-color: #0a0a0a;
    border-right: 1px solid #1a1a1a;
    box-shadow: 2px 0 20px rgba(0,0,0,0.35);
}

[data-testid="stMetric"] {
    background-color: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    padding: 1rem 1.25rem;
    transition: all 0.25s ease;
}
[data-testid="stMetric"]:hover {
    border-color: #a755f6 !important;
    transform: translateY(-2px);
}
[data-testid="stMetricValue"] {
    color: #39FF14 !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}
[data-testid="stMetricLabel"] {
    color: #888 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.stButton > button {
    background-color: #39FF14;
    color: #000000;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.85rem;
    padding: 0.5rem 1.25rem;
    transition: all 0.2s;
}
.stButton > button:hover {
    background-color: #a755f6;
    color: #ffffff;
    border: none;
}

.stTextInput > div > div > input,
.stSelectbox > div > div,
.stTextArea > div > div > textarea {
    background-color: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 6px !important;
    color: #e0e0e0 !important;
}

.streamlit-expanderHeader {
    background-color: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-weight: 500 !important;
}

h1 { color: #ffffff !important; font-weight: 700 !important; letter-spacing: -0.02em; }
h2 { color: #ffffff !important; font-weight: 600 !important; }
h3 { color: #e0e0e0 !important; font-weight: 500 !important; }

.stProgress > div > div > div { background-color: #a755f6 !important; }
hr { border-color: #2a2a2a !important; }

.stTable th {
    background-color: #111 !important;
    color: #888 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.stTable td { color: #e0e0e0 !important; font-size: 0.875rem !important; }

div[role="radiogroup"] label:hover { color: #a755f6 !important; transition: 0.2s ease; }
div[role="radiogroup"] input:checked + div { color: #39FF14 !important; font-weight: 700 !important; }
div[role="radiogroup"] label[data-baseweb="radio"] input { accent-color: #a755f6 !important; }

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
</style>
""", unsafe_allow_html=True)

PIPELINE = ["Prospecto","Analizado","Contactado","Conversación","Reunión","Propuesta","Negociación","Cliente","Perdido"]
SECTORES = ["Alimentos y bebidas","Salud natural","Belleza y cuidado personal","Salud y bienestar profesional","Servicios profesionales"]
CANALES  = ["WhatsApp","Email","Instagram","Facebook","Llamada","Reunión presencial"]
ESTADOS_PROPUESTA = ["En preparación","Enviada","Negociación","Aceptada","Rechazada"]
META = 5

# ── Session state para controlar formularios ─────────────
for key in ["show_form_prospecto","show_form_seguimiento","show_form_reunion","show_form_propuesta"]:
    if key not in st.session_state:
        st.session_state[key] = False

# ── SIDEBAR ──────────────────────────────────────────────
with st.sidebar:

    st.image(
        "logo.png",
        width=180
    )

    st.markdown("""
    <style>
    div[role="radiogroup"]{
        margin-top:-20px;
    }
            "Dashboard",
            "Prospectos",
            "Pipeline Kanban",
            "Seguimientos",
            "Reuniones",
            "Propuestas",
            "Clientes",
            "Calendario"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(f"""
<div style='padding: 8px 0;'>
    <div style='font-size:0.85rem;font-weight:600;color:#e0e0e0;'>
        {st.session_state.nombre}
    </div>
    <div style='font-size:0.7rem;color:#555;letter-spacing:0.05em;text-transform:uppercase;margin-top:2px;'>
        {st.session_state.rol}
    </div>
</div>
""", unsafe_allow_html=True)
    
# ── DASHBOARD ────────────────────────────────────────────
if pagina == "Dashboard":
    st.markdown("## Dashboard")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Resumen comercial · 2026</p>", unsafe_allow_html=True)

    db = get_session()
    prospectos    = db.query(Prospecto).all()
    seguimientos  = db.query(Seguimiento).all()
    clientes_db   = db.query(Cliente).all()
    db.close()

    prospectos_count = len([p for p in prospectos if p.estado_pipeline == "Prospecto"])
    analizados       = len([p for p in prospectos if p.estado_pipeline == "Analizado"])
    contactados      = len([p for p in prospectos if p.estado_pipeline == "Contactado"])
    conversaciones   = len([p for p in prospectos if p.estado_pipeline == "Conversación"])
    reuniones        = len([p for p in prospectos if p.estado_pipeline == "Reunión"])
    propuestas       = len([p for p in prospectos if p.estado_pipeline == "Propuesta"])
    negociacion      = len([p for p in prospectos if p.estado_pipeline == "Negociación"])
    clientes         = len([p for p in prospectos if p.estado_pipeline == "Cliente"])
    seguimientos_pendientes = len([s for s in seguimientos if not s.completado])
    mrr_total        = sum(c.fee_mensual for c in clientes_db if c.estado == "Activo")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Prospectos",    prospectos_count)
    c2.metric("Analizados",    analizados)
    c3.metric("Contactados",   contactados)
    c4.metric("Conversaciones",conversaciones)

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Reuniones",   reuniones)
    c6.metric("Propuestas",  propuestas)
    c7.metric("Negociación", negociacion)
    c8.metric("Clientes",    clientes)

    c9, c10 = st.columns(2)
    c9.metric("MRR Total", f"${mrr_total:,.0f}")
    c10.metric("Seguimientos Pendientes", seguimientos_pendientes)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**Meta anual · {clientes} de {META} clientes**")
    st.progress(min(clientes / META, 1.0))
    if clientes < META:
        st.caption(f"Faltan {META - clientes} cliente(s) para alcanzar la meta.")
    else:
        st.success("Meta alcanzada.")

    st.markdown("---")
    st.markdown("### Prospectos recientes")
    db = get_session()
    recientes = db.query(Prospecto).order_by(Prospecto.fecha_registro.desc()).limit(10).all()
    db.close()
    if recientes:
        st.table([{"Empresa": p.empresa, "Contacto": p.contacto or "—",
                   "Sector": p.sector or "—", "Estado": p.estado_pipeline,
                   "Registro": str(p.fecha_registro)} for p in recientes])
    else:
        st.caption("Sin prospectos registrados aún.")

# ── PROSPECTOS ───────────────────────────────────────────
elif pagina == "Prospectos":
    st.markdown("## Prospectos")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Gestión de contactos comerciales</p>", unsafe_allow_html=True)

    if st.button("+ Agregar prospecto"):
        st.session_state.show_form_prospecto = True

    if st.session_state.show_form_prospecto:
        with st.form("form_prospecto"):
            c1, c2 = st.columns(2)
            empresa   = c1.text_input("Empresa")
            contacto  = c2.text_input("Nombre del contacto")
            c3, c4 = st.columns(2)
            telefono  = c3.text_input("Teléfono")
            email     = c4.text_input("Email")
            c5, c6 = st.columns(2)
            whatsapp  = c5.text_input("WhatsApp")
            instagram = c6.text_input("Instagram")
            c7, c8 = st.columns(2)
            facebook  = c7.text_input("Facebook")
            ubicacion = c8.text_input("Ubicación")
            c9, c10 = st.columns(2)
            sector = c9.selectbox("Sector", SECTORES)
            estado = c10.selectbox("Estado en pipeline", PIPELINE)
            ca, cb = st.columns([1, 1])
            guardar   = ca.form_submit_button("Guardar")
            cancelar  = cb.form_submit_button("Cancelar")

            if cancelar:
                st.session_state.show_form_prospecto = False
                st.rerun()
            if guardar:
                if not empresa:
                    st.error("El nombre de la empresa es obligatorio.")
                else:
                    db = get_session()
                    db.add(Prospecto(
                        empresa=empresa, contacto=contacto, telefono=telefono,
                        email=email, whatsapp=whatsapp, instagram=instagram,
                        facebook=facebook, ubicacion=ubicacion,
                        sector=sector, estado_pipeline=estado,
                        fecha_registro=date.today()
                    ))
                    db.commit(); db.close()
                    st.session_state.show_form_prospecto = False
                    st.rerun()

    st.markdown("---")
    db = get_session()
    prospectos = db.query(Prospecto).order_by(Prospecto.fecha_registro.desc()).all()
    db.close()

    if not prospectos:
        st.caption("No hay prospectos registrados.")
    else:
        for p in prospectos:
            with st.expander(f"{p.empresa}  ·  {p.estado_pipeline}"):
                c1, c2, c3 = st.columns(3)
                c1.markdown(f"**Contacto** · {p.contacto or '—'}")
                c1.markdown(f"**Teléfono** · {p.telefono or '—'}")
                c1.markdown(f"**Email** · {p.email or '—'}")
                c2.markdown(f"**WhatsApp** · {p.whatsapp or '—'}")
                c2.markdown(f"**Instagram** · {p.instagram or '—'}")
                c2.markdown(f"**Facebook** · {p.facebook or '—'}")
                c3.markdown(f"**Sector** · {p.sector or '—'}")
                c3.markdown(f"**Ubicación** · {p.ubicacion or '—'}")
                c3.markdown(f"**Registrado** · {p.fecha_registro}")
                st.markdown("<br>", unsafe_allow_html=True)
                db2 = get_session()
                col_a, col_b, col_c = st.columns([3, 1, 1])
                nuevo_estado = col_a.selectbox("Cambiar estado", PIPELINE,
                    index=PIPELINE.index(p.estado_pipeline), key=f"estado_{p.id}")
                if col_b.button("Actualizar", key=f"btn_{p.id}"):
                    pr = db2.query(Prospecto).get(p.id)
                    pr.estado_pipeline = nuevo_estado
                    db2.commit(); db2.close(); st.rerun()
                if col_c.button("Eliminar", key=f"del_{p.id}"):
                    pr = db2.query(Prospecto).get(p.id)
                    db2.delete(pr); db2.commit(); db2.close(); st.rerun()

# ── KANBAN ───────────────────────────────────────────────
elif pagina == "Pipeline Kanban":
    st.markdown("## Pipeline Kanban")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Mueve los prospectos entre etapas con las flechas</p>", unsafe_allow_html=True)
    db = get_session()
    prospectos = db.query(Prospecto).all()
    db.close()
    etapas = [e for e in PIPELINE if e != "Perdido"]
    cols   = st.columns(len(etapas))
    for i, etapa in enumerate(etapas):
        grupo = [p for p in prospectos if p.estado_pipeline == etapa]
        with cols[i]:
            color = ("#39FF14" if etapa in ["Contactado","Conversación","Reunión","Cliente"]
                     else "#a755f6" if etapa in ["Propuesta","Negociación"] else "#888888")
            st.markdown(f"""
            <div style='font-size:0.7rem;font-weight:600;text-transform:uppercase;
                        letter-spacing:0.08em;color:{color};margin-bottom:4px;'>{etapa}</div>
            <div style='font-size:0.75rem;color:#555;margin-bottom:8px;'>{len(grupo)}</div>
            <hr style='border-color:#1e1e1e;margin-bottom:8px;'>
            """, unsafe_allow_html=True)
            for p in grupo:
                with st.container(border=True):
                    st.markdown(f"<div style='font-size:0.85rem;font-weight:600;color:#fff'>{p.empresa}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='font-size:0.75rem;color:#666;margin-bottom:6px'>{p.sector or ''}</div>", unsafe_allow_html=True)
                    idx = PIPELINE.index(etapa)
                    b1, b2 = st.columns(2)
                    if idx > 0:
                        if b1.button("←", key=f"back_{p.id}_{etapa}", use_container_width=True):
                            db2 = get_session()
                            pr  = db2.query(Prospecto).get(p.id)
                            pr.estado_pipeline = PIPELINE[idx - 1]
                            db2.commit(); db2.close(); st.rerun()
                    if idx < len(PIPELINE) - 2:
                        if b2.button("→", key=f"fwd_{p.id}_{etapa}", use_container_width=True):
                            db2 = get_session()
                            pr  = db2.query(Prospecto).get(p.id)
                            pr.estado_pipeline = PIPELINE[idx + 1]
                            db2.commit(); db2.close(); st.rerun()

# ── SEGUIMIENTOS ─────────────────────────────────────────
elif pagina == "Seguimientos":
    st.markdown("## Seguimientos")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Próximos contactos programados</p>", unsafe_allow_html=True)

    if st.button("+ Registrar seguimiento"):
        st.session_state.show_form_seguimiento = True

    if st.session_state.show_form_seguimiento:
        db = get_session()
        prospectos = db.query(Prospecto).order_by(Prospecto.empresa).all()
        db.close()
        if not prospectos:
            st.warning("Primero agrega un prospecto.")
        else:
            with st.form("form_seguimiento"):
                opciones = {p.empresa: p.id for p in prospectos}
                c1, c2 = st.columns(2)
                empresa_sel = c1.selectbox("Prospecto", list(opciones.keys()))
                canal       = c2.selectbox("Canal", CANALES)
                c3, c4 = st.columns(2)
                fecha_prox  = c3.date_input("Fecha próximo contacto", value=date.today())
                completado  = c4.checkbox("Marcar como completado")
                comentario  = st.text_area("Comentario")
                ca, cb = st.columns([1, 1])
                guardar  = ca.form_submit_button("Guardar")
                cancelar = cb.form_submit_button("Cancelar")
                if cancelar:
                    st.session_state.show_form_seguimiento = False
                    st.rerun()
                if guardar:
                    db = get_session()
                    db.add(Seguimiento(
                        prospecto_id=opciones[empresa_sel],
                        fecha_proxima=fecha_prox,
                        canal=canal,
                        comentario=comentario,
                        completado=completado
                    ))
                    db.commit(); db.close()
                    st.session_state.show_form_seguimiento = False
                    st.rerun()

    st.markdown("---")
    db = get_session()
    seguimientos = db.query(Seguimiento).order_by(Seguimiento.fecha_proxima).all()
    db.close()

    if not seguimientos:
        st.caption("No hay seguimientos registrados.")
    else:
        pendientes  = [s for s in seguimientos if not s.completado]
        completados = [s for s in seguimientos if s.completado]

        if pendientes:
            st.markdown("**Pendientes**")
            for s in pendientes:
                db2 = get_session()
                p   = db2.query(Prospecto).get(s.prospecto_id)
                nombre = p.empresa if p else "—"
                db2.close()
                with st.container(border=True):
                    c1, c2, c3, c4 = st.columns([3, 2, 1, 1])
                    c1.markdown(f"**{nombre}**  ·  {s.canal}")
                    c2.markdown(f"`{s.fecha_proxima}`")
                    if s.comentario:
                        st.caption(s.comentario)
                    if c3.button("Completar", key=f"comp_{s.id}"):
                        db2 = get_session()
                        seg = db2.query(Seguimiento).get(s.id)
                        seg.completado = True
                        db2.commit(); db2.close(); st.rerun()
                    if c4.button("Eliminar", key=f"delseg_{s.id}"):
                        db2 = get_session()
                        seg = db2.query(Seguimiento).get(s.id)
                        db2.delete(seg); db2.commit(); db2.close(); st.rerun()

        if completados:
            st.markdown("---")
            st.markdown("**Completados**")
            for s in completados:
                db2 = get_session()
                p   = db2.query(Prospecto).get(s.prospecto_id)
                nombre = p.empresa if p else "—"
                db2.close()
                st.markdown(f"<div style='color:#444;font-size:0.85rem;padding:6px 0;border-bottom:1px solid #1e1e1e'>{nombre}  ·  {s.canal}  ·  {s.fecha_proxima}</div>", unsafe_allow_html=True)

# ── REUNIONES ────────────────────────────────────────────
elif pagina == "Reuniones":
    st.markdown("## Reuniones")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Registro de reuniones y próximos pasos</p>", unsafe_allow_html=True)

    if st.button("+ Registrar reunión"):
        st.session_state.show_form_reunion = True

    if st.session_state.show_form_reunion:
        db = get_session()
        prospectos = db.query(Prospecto).order_by(Prospecto.empresa).all()
        db.close()
        if not prospectos:
            st.warning("Primero agrega un prospecto.")
        else:
            with st.form("form_reunion"):
                opciones = {p.empresa: p.id for p in prospectos}
                c1, c2 = st.columns(2)
                empresa_sel   = c1.selectbox("Prospecto", list(opciones.keys()))
                fecha_reunion = c2.date_input("Fecha de la reunión", value=date.today())
                resultado     = st.text_area("Resultado de la reunión", placeholder="Ej: Interesado en branding y redes sociales.")
                proximo_paso  = st.text_area("Próximo paso", placeholder="Ej: Enviar propuesta antes del viernes.")
                ca, cb = st.columns([1, 1])
                guardar  = ca.form_submit_button("Guardar")
                cancelar = cb.form_submit_button("Cancelar")
                if cancelar:
                    st.session_state.show_form_reunion = False
                    st.rerun()
                if guardar:
                    db = get_session()
                    db.add(Reunion(
                        prospecto_id=opciones[empresa_sel],
                        fecha=fecha_reunion,
                        resultado=resultado,
                        proximo_paso=proximo_paso
                    ))
                    db.commit(); db.close()
                    st.session_state.show_form_reunion = False
                    st.rerun()

    st.markdown("---")
    db = get_session()
    reuniones = db.query(Reunion).order_by(Reunion.fecha.desc()).all()
    db.close()

    if not reuniones:
        st.caption("No hay reuniones registradas.")
    else:
        for r in reuniones:
            db2 = get_session()
            p   = db2.query(Prospecto).get(r.prospecto_id)
            nombre = p.empresa if p else "—"
            db2.close()
            with st.container(border=True):
                c1, c2, c3 = st.columns([1, 4, 1])
                c1.markdown(f"<div style='color:#888;font-size:0.8rem'>{r.fecha}</div>", unsafe_allow_html=True)
                c2.markdown(f"**{nombre}**")
                if r.resultado:
                    st.markdown(f"<div style='font-size:0.875rem;color:#ccc;margin-top:4px'>{r.resultado}</div>", unsafe_allow_html=True)
                if r.proximo_paso:
                    st.markdown(f"<div style='font-size:0.8rem;color:#a755f6;margin-top:4px'>Próximo paso · {r.proximo_paso}</div>", unsafe_allow_html=True)
                if c3.button("Eliminar", key=f"delreu_{r.id}"):
                    db2 = get_session()
                    reu = db2.query(Reunion).get(r.id)
                    db2.delete(reu); db2.commit(); db2.close(); st.rerun()

# ── PROPUESTAS ───────────────────────────────────────────
elif pagina == "Propuestas":
    st.markdown("## Propuestas")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Gestión de propuestas comerciales</p>", unsafe_allow_html=True)

    if st.button("+ Registrar propuesta"):
        st.session_state.show_form_propuesta = True

    if st.session_state.show_form_propuesta:
        db = get_session()
        prospectos = db.query(Prospecto).order_by(Prospecto.empresa).all()
        db.close()
        if not prospectos:
            st.warning("Primero agrega un prospecto.")
        else:
            with st.form("form_propuesta"):
                opciones = {p.empresa: p.id for p in prospectos}
                c1, c2 = st.columns(2)
                empresa_sel = c1.selectbox("Prospecto", list(opciones.keys()))
                servicio    = c2.text_input("Servicio", placeholder="Ej: Gestión de redes sociales")
                c3, c4 = st.columns(2)
                monto       = c3.number_input("Monto mensual ($)", min_value=0.0, step=100.0)
                fecha_envio = c4.date_input("Fecha de envío", value=date.today())
                estado      = st.selectbox("Estado", ESTADOS_PROPUESTA)
                ca, cb = st.columns([1, 1])
                guardar  = ca.form_submit_button("Guardar")
                cancelar = cb.form_submit_button("Cancelar")
                if cancelar:
                    st.session_state.show_form_propuesta = False
                    st.rerun()
                if guardar:
                    db = get_session()
                    nueva = Propuesta(
                        prospecto_id=opciones[empresa_sel],
                        servicio=servicio, monto=monto,
                        fecha_envio=fecha_envio, estado=estado
                    )
                    db.add(nueva)
                    db.commit()
                    if estado == "Aceptada":
                        ya_cliente = db.query(Cliente).filter_by(prospecto_id=opciones[empresa_sel]).first()
                        if not ya_cliente:
                            db.add(Cliente(
                                prospecto_id=opciones[empresa_sel],
                                fecha_inicio=date.today(),
                                servicio_contratado=servicio,
                                fee_mensual=monto, estado="Activo"
                            ))
                            prosp = db.query(Prospecto).get(opciones[empresa_sel])
                            prosp.estado_pipeline = "Cliente"
                            db.commit()
                    db.close()
                    st.session_state.show_form_propuesta = False
                    st.rerun()

    st.markdown("---")
    db = get_session()
    propuestas = db.query(Propuesta).order_by(Propuesta.fecha_envio.desc()).all()
    db.close()

    if not propuestas:
        st.caption("No hay propuestas registradas.")
    else:
        for pr in propuestas:
            db2 = get_session()
            p   = db2.query(Prospecto).get(pr.prospecto_id)
            nombre = p.empresa if p else "—"
            db2.close()
            color_estado = {
                "Aceptada": "#39FF14", "Rechazada": "#ff4444",
                "Negociación": "#a755f6", "Enviada": "#888", "En preparación": "#555"
            }.get(pr.estado, "#888")
            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 2, 2])
                c1.markdown(f"**{nombre}**  ·  {pr.servicio or '—'}")
                c2.markdown(f"<span style='color:#39FF14;font-weight:700'>${pr.monto:,.0f}</span>  ·  {pr.fecha_envio}", unsafe_allow_html=True)
                c3.markdown(f"<span style='color:{color_estado};font-size:0.8rem;font-weight:600'>{pr.estado}</span>", unsafe_allow_html=True)

                # Cambiar estado
                db2 = get_session()
                col_e, col_a, col_d = st.columns([3, 1, 1])
                nuevo_estado = col_e.selectbox("Cambiar estado", ESTADOS_PROPUESTA,
                    index=ESTADOS_PROPUESTA.index(pr.estado), key=f"est_pr_{pr.id}")
                if col_a.button("Actualizar", key=f"upd_pr_{pr.id}"):
                    prop = db2.query(Propuesta).get(pr.id)
                    prop.estado = nuevo_estado
                    db2.commit()
                    # Convertir a cliente si se acepta
                    if nuevo_estado == "Aceptada":
                        ya = db2.query(Cliente).filter_by(prospecto_id=pr.prospecto_id).first()
                        if not ya:
                            db2.add(Cliente(
                                prospecto_id=pr.prospecto_id,
                                fecha_inicio=date.today(),
                                servicio_contratado=pr.servicio,
                                fee_mensual=pr.monto, estado="Activo"
                            ))
                            prosp = db2.query(Prospecto).get(pr.prospecto_id)
                            prosp.estado_pipeline = "Cliente"
                            db2.commit()
                    db2.close(); st.rerun()
                if col_d.button("Eliminar", key=f"del_pr_{pr.id}"):
                    db2.delete(db2.query(Propuesta).get(pr.id))
                    db2.commit(); db2.close(); st.rerun()

# ── CLIENTES ─────────────────────────────────────────────
elif pagina == "Clientes":
    st.markdown("## Clientes")
    st.markdown("<p style='color:#666;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem'>Clientes activos de ZENIT</p>", unsafe_allow_html=True)
    db = get_session()
    clientes = db.query(Cliente).order_by(Cliente.fecha_inicio.desc()).all()
    db.close()

    if not clientes:
        st.caption("Aún no hay clientes. Se agregan automáticamente al aceptar una propuesta.")
    else:
        total_mrr = sum(c.fee_mensual for c in clientes if c.estado == "Activo")
        st.markdown(f"<div style='font-size:0.85rem;color:#888;margin-bottom:1rem'>MRR total · <span style='color:#39FF14;font-weight:700'>${total_mrr:,.0f}</span></div>", unsafe_allow_html=True)
        st.markdown("---")
        for c in clientes:
            db2 = get_session()
            p   = db2.query(Prospecto).get(c.prospecto_id)
            nombre = p.empresa if p else "—"
            db2.close()
            color = "#39FF14" if c.estado == "Activo" else "#555"
            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 2, 1])
                c1.markdown(f"**{nombre}**")
                c1.markdown(f"<div style='font-size:0.8rem;color:#888'>{c.servicio_contratado or '—'}</div>", unsafe_allow_html=True)
                c2.markdown(f"<span style='color:#39FF14;font-weight:700'>${c.fee_mensual:,.0f}</span> / mes", unsafe_allow_html=True)
                c2.markdown(f"<div style='font-size:0.8rem;color:#888'>Desde {c.fecha_inicio}</div>", unsafe_allow_html=True)
                c3.markdown(f"<span style='color:{color};font-size:0.8rem;font-weight:600'>{c.estado}</span>", unsafe_allow_html=True)
    
# ── CALENDARIO ───────────────────────────────────────────
elif pagina == "Calendario":

    st.markdown("## Calendario Comercial")

    st.markdown(
        """
        Gestiona actividades comerciales.
        """
    )

    st.link_button(
        "📂 Abrir Calendario",
        "https://docs.google.com/spreadsheets/d/1-RuXa-pYtsZh5ZcW-2NuDKprQo3WgPGg9wQssD6ireg/edit?gid=0#gid=0",
        use_container_width=True
    )