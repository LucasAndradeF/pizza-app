from flask import Blueprint, jsonify, request
from .models import Produto, Pizza, Pedido, Usuario, Bebidas, Doces
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

pizzaria_bp = Blueprint("pizzaria", __name__)


@pizzaria_bp.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome or not email or not senha:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado"}), 400

    senha_hash = generate_password_hash(senha)
    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201


@pizzaria_bp.route("/login", methods=["POST"])
def login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not check_password_hash(usuario.senha, senha):
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"message": "Login realizado com sucesso!"}), 200


@pizzaria_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():

    usuarios = Usuario.query.all()

    lista_usuarios = [
        {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}
        for usuario in usuarios
    ]

    return jsonify(lista_usuarios), 200


@pizzaria_bp.route("/pizzas", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify(
        [
            {"id": p.id, "nome": p.nome, "recheio": p.recheio, "preco": p.preco}
            for p in pizzas
        ]
    )


@pizzaria_bp.route("/pizzas/<int:id>", methods=["GET"])
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"message": "Pizza não encontrada"}), 404
    return jsonify(
        {
            "id": pizza.id,
            "preco": pizza.preco,
            "recheio": pizza.recheio,
        }
    )


@pizzaria_bp.route("/pizzas", methods=["POST"])
def create_pizza():
    data = request.get_json()

    if not all(key in data for key in ["nome", "preco", "recheio"]):
        return jsonify({"message": "Campos obrigatórios faltando"}), 400

    new_pizza = Pizza(
        nome=data["nome"],
        preco=data["preco"],
        recheio=data["recheio"],
    )
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify({"message": "Pizza criada com sucesso"}), 201


@pizzaria_bp.route("/pizzas/<int:id>", methods=["PUT"])
def update_pizza(id):
    data = request.get_json()
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"message": "Pizza não encontrada"}), 404
    pizza.nome = data["nome"]
    pizza.preco = data["preco"]
    pizza.recheio = data["recheio"]
    db.session.commit()
    return jsonify({"message": "Pizza atualizada com sucesso"})


@pizzaria_bp.route("/pizzas/<int:id>", methods=["DELETE"])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"message": "Pizza não encontrada"}), 404
    db.session.delete(pizza)
    db.session.commit()
    return jsonify({"message": "Pizza deletada com sucesso"})



@pizzaria_bp.route("/bebidas", methods=["GET"])
def get_bebidas():
    bebidas = Bebidas.query.all()
    return jsonify(
        [
            {"id": p.id, "nome": p.nome, "preco": p.preco}
            for p in bebidas
        ]
    )

@pizzaria_bp.route("/bebidas/<int:id>", methods=["GET"])
def get_bebida(id):
    bebida = Bebidas.query.get(id)
    if not bebida:
        return jsonify({"message": "Bebida não encontrada"}), 404
    return jsonify(
        {
            "id": bebida.id,
            "nome": bebida.nome,
            "preco": bebida.preco,
        }
    )


@pizzaria_bp.route("/bebidas", methods=["POST"])
def create_bebida():
    data = request.get_json()

    if not all(key in data for key in ["nome", "preco"]):
        return jsonify({"message": "Campos obrigatórios faltando"}), 400

    new_bebida = Bebidas(
        nome=data["nome"],
        preco=data["preco"],
    )
    db.session.add(new_bebida)
    db.session.commit()
    return jsonify({"message": "Bebida criada com sucesso"}), 201


@pizzaria_bp.route("/bebidas/<int:id>", methods=["PUT"])
def update_bebida(id):
    data = request.get_json()
    bebida = Bebidas.query.get(id)
    if not bebida:
        return jsonify({"message": "Bebida não encontrada"}), 404
    bebida.nome = data["nome"]
    bebida.preco = data["preco"]
    db.session.commit()
    return jsonify({"message": "Bebida atualizada com sucesso"})


@pizzaria_bp.route("/bebidas/<int:id>", methods=["DELETE"])
def delete_bebida(id):
    bebida = Bebidas.query.get(id)
    if not bebida:
        return jsonify({"message": "Bebida não encontrada"}), 404
    db.session.delete(bebida)
    db.session.commit()
    return jsonify({"message": "Bebida deletada com sucesso"})


@pizzaria_bp.route("/doces", methods=["GET"])
def get_doces():
    doces = Doces.query.all()
    return jsonify(
        [
            {"id": d.id, "nome": d.nome, "preco": d.preco}
            for d in doces
        ]
    )


@pizzaria_bp.route("/doces/<int:id>", methods=["GET"])
def get_doce(id):
    doce = Doces.query.get(id)
    if not doce:
        return jsonify({"message": "Doce não encontrado"}), 404
    return jsonify(
        {
            "id": doce.id,
            "nome": doce.nome,
            "preco": doce.preco,
        }
    )


@pizzaria_bp.route("/doces", methods=["POST"])
def create_doce():
    data = request.get_json()

    if not all(key in data for key in ["nome", "preco"]):
        return jsonify({"message": "Campos obrigatórios faltando"}), 400

    new_doce = Doces(
        nome=data["nome"],
        preco=data["preco"],
    )
    db.session.add(new_doce)
    db.session.commit()
    return jsonify({"message": "Doce criado com sucesso"}), 201


@pizzaria_bp.route("/doces/<int:id>", methods=["PUT"])
def update_doce(id):
    data = request.get_json()
    doce = Doces.query.get(id)
    if not doce:
        return jsonify({"message": "Doce não encontrado"}), 404
    doce.nome = data["nome"]
    doce.preco = data["preco"]
    db.session.commit()
    return jsonify({"message": "Doce atualizado com sucesso"})


@pizzaria_bp.route("/doces/<int:id>", methods=["DELETE"])
def delete_doce(id):
    doce = Doces.query.get(id)
    if not doce:
        return jsonify({"message": "Doce não encontrado"}), 404
    db.session.delete(doce)
    db.session.commit()
    return jsonify({"message": "Doce deletado com sucesso"})


@pizzaria_bp.route("/pedidos", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data or "produto_id" not in data:
        return (
            jsonify({"message": "Dados inválidos, campo produto_id é necessário"}),
            400,
        )
    produto = Produto.query.get(data["produto_id"])
    if not produto:
        return jsonify({"message": "Produto não encontrado"}), 404
    new_order = Pedido(produto_id=data["produto_id"], status="Pendente")
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Pedido criado com sucesso", "id": new_order.id}), 201


@pizzaria_bp.route("/pedidos/<int:id>", methods=["PUT"])
def update_order(id):
    data = request.get_json()
    order = Pedido.query.get(id)
    if not order:
        return jsonify({"message": "Pedido não encontrado"}), 404
    if "status" in data:
        order.status = data["status"]
        db.session.commit()
        return jsonify({"message": "Pedido atualizado com sucesso"})
    return jsonify({"message": "Status não fornecido"}), 400


@pizzaria_bp.route("/pedidos", methods=["GET"])
def get_orders():
    orders = Pedido.query.all()
    return jsonify(
        [{"id": o.id, "produto_id": o.produto_id, "status": o.status} for o in orders]
    )
