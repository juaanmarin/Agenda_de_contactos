from flask import Flask, render_template, request, redirect,url_for, flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PORT"] = 3307 
app.config["MYSQL_PASSWORD"] = "nuviavelasquez07"
app.config["MYSQL_DB"] = "agenda_contactos"
mysql = MySQL(app)

app.secret_key = "mysesion"

@app.route("/")
def index():
    cur= mysql.connection.cursor()
    cur.execute("select * from agenda_contactos.contactos;")
    data = cur.fetchall()
    return render_template("index.html", contactos=data)

@app.route("/añadir_contacto", methods=["POST"])
def añadir_contacto():
    if (request.method=="POST"):
        nombre=request.form["nombre"]
        numero=request.form["telefono"]
        email=request.form["email"]
        cur=mysql.connection.cursor()
        cur.execute("insert into contactos (nombre, telefono, email) values (%s, %s, %s)", (nombre,numero,email))
        mysql.connection.commit()
        flash("contacto registrado")
    return redirect(url_for("index"))

@app.route("/editar_contacto/<id>")
def editar_contacto(id):
    cur=mysql.connection.cursor()
    cur.execute("select * from contactos where id=(%s)", (id,))
    dato=cur.fetchall()
    return render_template("Editar_contactos.html", contacto=dato[0])

@app.route("/editar/<id>", methods=["POST"])
def editar_contactos(id):
    print("***************")
    if(request.method=="POST"):
        nombre=request.form["nombre"]
        numero=request.form["telefono"]
        email=request.form["email"]
        cur=mysql.connection.cursor()
        cur.execute("update contactos set nombre=(%s), telefono=(%s), email=(%s) where id=(%s)",(nombre,numero,email,id))
        flash("contacto actualizado")
        mysql.connection.commit()
        print("***************")
        return redirect(url_for("index"))

@app.route("/eliminar_contacto/<string:id>")
def eliminar_contacto(id):
    cur=mysql.connection.cursor()
    cur.execute("delete from contactos where id=(%s)", (id,))
    #cur.execute("delete from contactos where id={0}", format(id))
    mysql.connection.commit()
    flash("contacto eliminado")
    return redirect(url_for("index"))


if(__name__=="__main__"):
    app.run(port=5000, debug=True)