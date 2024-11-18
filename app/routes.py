from flask import Blueprint, jsonify, request
from .models import Produto, Pizza, Pedido, Usuario
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


# Rota de login
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
            {"id": p.id, "nome": p.nome, "preco": p.preco, "tamanho": p.tamanho}
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
            "nome": pizza.nome,
            "preco": pizza.preco,
            "tamanho": pizza.tamanho,
        }
    )


@pizzaria_bp.route("/pizzas", methods=["POST"])
def create_pizza():
    data = request.get_json()

    # Verificar se os campos obrigatórios estão presentes
    if not all(
        key in data for key in ["nome", "preco", "tamanho", "descricao", "tipo"]
    ):
        return jsonify({"message": "Campos obrigatórios faltando"}), 400

    new_pizza = Pizza(
        nome=data["nome"],
        preco=data["preco"],
        tamanho=data["tamanho"],
        descricao=data["descricao"],
        tipo=data["tipo"],
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
    pizza.tamanho = data["tamanho"]
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
