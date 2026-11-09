from database.database import obtener_conexion


def registrar_producto(nombre, descripcion, precio, categoria_id):
    conexion = obtener_conexion()

    try:
        conexion.execute(
            """
            INSERT INTO productos (nombre, descripcion, precio, categoria_id)
            VALUES (?, ?, ?, ?)
            """,
            (nombre, descripcion, precio, categoria_id)
        )
        conexion.commit()
        return True

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def listar_productos():
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            SELECT productos.*, categorias.nombre AS categoria
            FROM productos
            LEFT JOIN categorias
            ON productos.categoria_id = categorias.id
            ORDER BY productos.nombre
            """
        )
        return [dict(fila) for fila in resultado.fetchall()]

    finally:
        conexion.close()


def actualizar_producto(id_producto, nombre, descripcion, precio, categoria_id):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            UPDATE productos
            SET nombre = ?, descripcion = ?, precio = ?, categoria_id = ?
            WHERE id = ?
            """,
            (nombre, descripcion, precio, categoria_id, id_producto)
        )
        conexion.commit()
        return resultado.rowcount > 0

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def eliminar_producto(id_producto):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            "DELETE FROM productos WHERE id = ?",
            (id_producto,)
        )
        conexion.commit()
        return resultado.rowcount > 0

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()