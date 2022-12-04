from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect
from models.cliente import Cadastrocliente
from conection.conexao import *


db.create_all()
db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/orcamentos",defaults={'id':0})
@app.route("/orcamentos/<id>")
def orcamentos(id):
    resultado = Cadastrocliente.query.filter_by(id=id).all()
    todos = Cadastrocliente.query.all()
    return render_template("orcamentos.html", resultado=resultado, todos=todos)


@app.route("/cadastro_clientes")
def cadastro_clientes():
    return render_template("cadastro_clientes.html")

@app.route("/orcamento")
def orcamento():
    return render_template("orcamento.html")

@app.route("/editar_clientes/<int:id>", methods=["POST", "GET"])
def editar_clientes(id):
    cliente = Cadastrocliente.query.filter(Cadastrocliente.id == id).first()
    return render_template("editar_clientes.html", cliente=cliente)


@app.route("/listar_clientes")
def listar_clientes():
    clientes = Cadastrocliente.query.all()
    return render_template("listar_clientes.html", clientes=clientes)


@app.route("/cadastro", methods=["POST"])
def cadastro():
    if request.method == "POST":
        if (
            request.form["nome"]
            and request.form["razao_social"]
            and request.form["cnpj_cpf"]
            and request.form["cep"]
            and request.form["rua"]
            and request.form["numero"]
            and request.form["bairro"]
            and request.form["cidade"]
            and request.form["uf"]
            and request.form["email"]
            and request.form["telefone"]
        ):
            cliente = Cadastrocliente(
                request.form["nome"],
                request.form["razao_social"],
                request.form["cnpj_cpf"],
                request.form["cep"],
                request.form["rua"],
                request.form["numero"],
                request.form["bairro"],
                request.form["cidade"],
                request.form["uf"],
                request.form["email"],
                request.form["telefone"],
            )
            db.session.add(cliente)
            db.session.commit()
            return render_template(
                "cadastro_clientes.html", mensagem="Cadastro efetuado com sucesso!"
            )
        else:
            return render_template(
                "cadastro_clientes.html", mensagem="Erro no cadastro!"
            )

@app.route("/atualizar", methods=["POST"])
def atualizar():
    if request.method == "POST":
        if (
            request.form["id"]
            and request.form["nome"]
            and request.form["razao_social"]
            and request.form["cnpj_cpf"]
            and request.form["cep"]
            and request.form["rua"]
            and request.form["numero"]
            and request.form["bairro"]
            and request.form["cidade"]
            and request.form["uf"]
            and request.form["email"]
            and request.form["telefone"]
        ):
            cliente = Cadastrocliente.query.filter(
                Cadastrocliente.id == request.form["id"]
            ).first()
            cliente.nome = request.form["nome"]
            cliente.razao_social = request.form["razao_social"]
            cliente.cnpj_cpf = request.form["cnpj_cpf"]
            cliente.cep = request.form["cep"]
            cliente.rua = request.form["rua"]
            cliente.numero = request.form["numero"]
            cliente.bairro = request.form["bairro"]
            cliente.cidade = request.form["cidade"]
            cliente.uf = request.form["uf"]
            cliente.email = request.form["email"]
            cliente.telefone = request.form["telefone"]
            db.session.add(cliente)
            db.session.commit()
            flash("Atualizado com sucesso!")
            return redirect(url_for("listar_clientes"))
        else:
            return render_template(
                "listar_clientes.html", mensagem="Erro na atualização!"
            )

@app.route('/delete_cliente/<id>')
def delete_cliente(id):
        user = Cadastrocliente.query.filter(Cadastrocliente.id==id).one()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("listar_clientes"))
    

if __name__ == "__main__":
    app.run()
