from flask import Flask, request, render_template, redirect, url_for
import pymysql
import time
import os

app  = Flask(__name__)

db_config = {
            "host":  "servidor-bd-ejemplo",
            "user": "root",
            "password": os.getenv("MYSQL_ROOT_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
            "connect_timeout": 3,
            "cursorclass": pymysql.cursors.DictCursor, #devuele los datos como diccionario para HTML 
            "autocommit": True
}

def obtener_conexion():
    max_retries = 10
    for attempt in range(max_retries):
        try:
            return pymysql.connect(**db_config)
        except pymysql.err.OperationalError as e:
            if attempt < max_retries - 1:
                print(f"Base de datos no lista aún. Esperando... (Intento {attempt + 1}/{max_retries})")
                time.sleep(3)
            else:
                raise e
def crear_tabla_si_no_existe():

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS aprendices (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            nombre_completo VARCHAR(100) NOT NULL,
            numero_documento VARCHAR(20) NOT NULL,
            ficha VARCHAR(20) NOT NULL,
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(sql)
            conn.commit()
            conn.close()
    except Exception as e:
        print(f"Error inicializando la base de datos: {e}")

crear_tabla_si_no_existe()


@app.route("/")
def main():
    bd_status = ""
    aprendices = []

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM aprendices ORDER BY id DESC")
            aprendices = cursor.fetchall()
        conn.close()
        bd_status = "CONEXION EXITOSA Y PRUEBA DE CI/CD y TEST EXITOSO"
    except Exception as e:
        bd_status = f"Error de conexión: {e}"

    return render_template("index.html", bd_status = bd_status, aprendices = aprendices)

@app.route("/registrar", methods=["POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form["nombre_completo"]
        documento = request.form["numero_documento"]
        ficha = request.form["ficha"]

        try: 
            conn = obtener_conexion()
            with conn.cursor() as cursor:
                sql = "INSERT INTO aprendices (nombre_completo, numero_documento, ficha) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, documento, ficha))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error al registrar: {e}")

        return redirect(url_for("main"))

if __name__== "__main__":
   # app.run(host="0.0.0.0", port = 5050, debug = True)
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    host = os.getenv("FLASK_HOST") or "0.0.0.0"  # nosec B104
    
    app.run(host=host, port=5050, debug=debug_mode)





# 	try:
# 		conn = pymysql.connect(
# 			host="servidor-bd",
# 			user="root",
# 			password="sena123",
# 			database="adso_db",
# 			connect_timeout=3
# 		)
# 		conn.close()
# 		bd_status = "CONEXION EXITOSA"


# 	except Exception as e:
# 		bd_status =f"Error al conectar {e}"

# 	return render_template("index.html",bd_status = bd_status)



# if __name__ == "__main__":
# 	app.run(host = "0.0.0.0", port = 5050,debug=True)

