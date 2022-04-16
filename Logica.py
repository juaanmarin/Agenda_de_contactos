class Logica:

    # def obteneConexion(app):
    #     app.config["MYSQL HOST"] = "localhost"
    #     app.config["MYSQL_USER"] = "root"
    #     app.config["MYSQL_PORT"] = 3307 
    #     app.config["MYSQL_PASSWORD"] = "nuviavelasquez07"
    #     app.config["MYSQL_DB"] = "agenda_contactos"
    #     mysql = MySQL(app)
    #     app.secret_key = "mysesion"

    def iniciar(mysql,):
        cur= mysql.connection.cursor()
        cur.execute("select * from agenda_contactos.contactos;") 
        return cur.fetchall()

    def añadirContactos(mysql,nombre,numero,email):
        cur=mysql.connection.cursor()
        cur.execute("insert into contactos (nombre, telefono, email) values (%s, %s, %s)", (nombre,numero,email))
        mysql.connection.commit()
        return 

    def obtenerContacto(mysql,id):
        cur=mysql.connection.cursor()
        cur.execute("select * from contactos where id=(%s)", (id,))
        return cur.fetchall()

    def editar(mysql,nombre,numero,email,id):
        cur=mysql.connection.cursor()
        cur.execute("update contactos set nombre=(%s), telefono=(%s), email=(%s) where id=(%s)",(nombre,numero,email,id))
        mysql.connection.commit()
        return

    def eliminar(mysql,id):
        cur=mysql.connection.cursor()
        cur.execute("delete from contactos where id=(%s)", (id,))
        mysql.connection.commit()