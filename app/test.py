from flask_sqlalchemy import db
import app

@app.route('/test_db')
def test_db():
    try:
        # Ejecuta una consulta simple
        result = db.session.execute('SELECT 1').scalar()
        if result == 1:
            return "Conexión a la base de datos exitosa."
        else:
            return "Conexión a la base de datos fallida."
    except Exception as e:
        return f"Error en la conexión a la base de datos: {str(e)}"