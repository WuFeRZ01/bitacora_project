

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS actividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL,
    responsable TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    condiciones_climaticas TEXT,
    usuario_id INTEGER NOT NULL,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS anexos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    ruta TEXT NOT NULL,
    actividad_id INTEGER NOT NULL,
    FOREIGN KEY(actividad_id) REFERENCES actividades(id)
);
