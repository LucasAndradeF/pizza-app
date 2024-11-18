from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
     

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    pedidos = db.relationship("Pedido", backref="produto", lazy=True)

    def __repr__(self):
        return f"<Produto {self.nome} - {self.tipo}>"


class Pizza(Produto):
    __tablename__ = "pizza"
    id = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key=True)
    recheio = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Pizza {self.nome} - {self.tamanho}>"

class Bebidas(Produto):
   __tablename__ = "bebidas"
   id = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key=True)
   
class Doces(Produto):
   __tablename__ = "doces"
   id = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key=True)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(20), default="Pendente")

    def __repr__(self):
        return f"<Pedido {self.id} - {self.status}>"

