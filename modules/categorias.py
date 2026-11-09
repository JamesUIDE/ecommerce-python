from database.database import obtener_conexion


def registrar_categoria(nombre, descripcion=""):
    conexion = obtener_conexion()

    try:
        conexion.execute(
            """
            INSERT INTO categorias (nombre, descripcion)
            VALUES (?, ?)
            """,
            (nombre, descripcion)
        )
        conexion.commit()
        return True

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def listar_categorias():
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            "SELECT * FROM categorias ORDER BY nombre"
        )
        return [dict(fila) for fila in resultado.fetchall()]

    finally:
        conexion.close()


def actualizar_categoria(id_categoria, nombre, descripcion=""):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            UPDATE categorias
            SET nombre = ?, descripcion = ?
            WHERE id = ?
            """,
            (nombre, descripcion, id_categoria)
        )
        conexion.commit()
        return resultado.rowcount > 0

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def eliminar_categoria(id_categoria):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            "DELETE FROM categorias WHERE id = ?",
            (id_categoria,)
        )
        conexion.commit()
        return resultado.rowcount > 0

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()