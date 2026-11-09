
from database.database import obtener_conexion


def consultar_inventario():
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            SELECT inventario.id,
                   productos.nombre AS producto,
                   inventario.cantidad
            FROM inventario
            INNER JOIN productos
            ON inventario.producto_id = productos.id
            ORDER BY productos.nombre
            """
        )
        return [dict(fila) for fila in resultado.fetchall()]

    finally:
        conexion.close()


def registrar_stock(producto_id, cantidad):
    conexion = obtener_conexion()

    try:
        conexion.execute(
            """
            INSERT INTO inventario (producto_id, cantidad)
            VALUES (?, ?)
            """,
            (producto_id, cantidad)
        )
        conexion.commit()
        return True

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def actualizar_stock(producto_id, nueva_cantidad):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            UPDATE inventario
            SET cantidad = ?
            WHERE producto_id = ?
            """,
            (nueva_cantidad, producto_id)
        )
        conexion.commit()
        return resultado.rowcount > 0

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def consultar_stock_bajo(limite=5):
    conexion = obtener_conexion()

    try:
        resultado = conexion.execute(
            """
            SELECT productos.nombre AS producto,
                   inventario.cantidad
            FROM inventario
            INNER JOIN productos
            ON inventario.producto_id = productos.id
            WHERE inventario.cantidad <= ?
            ORDER BY inventario.cantidad
            """,
            (limite,)
        )
        return [dict(fila) for fila in resultado.fetchall()]

    finally:
        conexion.close()
