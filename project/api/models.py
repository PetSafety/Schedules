from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import uuid

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"
    idusuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeCompleto = db.Column(db.Text, nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)

    def __init__(
            self,
            nomeCompleto,
            cpf,
            telefone
    ):
        self.nomeCompleto = nomeCompleto
        self.cpf = cpf
        self.telefone = telefone

    def to_json(self):
        return {
            "idusuario": self.idusuario,
            "nomeCompleto": self.nomeCompleto,
            "cpf": self.cpf
        }


class Relatorio(db.Model):
    __tablename__ = "relatorio"
    idrelatorio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dadosRelatorio = db.Column(postgresql.JSON)

    def __init__(
            self,
            dadosRelatorio
    ):
        self.dadosRelatorio = dadosRelatorio

    def to_json(self):
        return {
            "idrelatorio": self.idrelatorio,
            "dadosRelatorio": self.dadosRelatorio
        }


class Transporte(db.Model):
    __tablename__ = "transporte"

    idtransporte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomepet = db.Column(db.Text, nullable=False)
    tipopet = db.Column(db.Enum('Cachorro', 'Gato'), nullable=False)
    dataViagem = db.Column(db.Date, nullable=False)
    origem = db.Column(db.Text, nullable=False)
    destino = db.Column(db.Text, nullable=False)
    idusuario = db.Column(db.Integer, db.ForeignKey("usuario.idusuario"))
    idrelatorio = db.Column(db.Integer, db.ForeignKey("relatorio.idrelatorio"))

    def __init__(
            self,
            nomepet,
            tipopet,
            dataViagem,
            origem,
            destino,
            idusuario,
            idrelatorio
    ):
        self.nomepet = nomepet
        self.tipopet = tipopet
        self.dataViagem = dataViagem
        self.origem = origem
        self.destino = destino
        self.idusuario = idusuario
        self.idrelatorio = idrelatorio

    def to_json(self):
        return {
            "idtransporte": self.idtransporte,
            "nomepet": self.nomepet,
            "tipopet": self.tipopet,
            "dataViagem": self.dataViagem,
            "origem": self.origem,
            "destino": self.destino,
            "idusuario": self.idusuario,
            "idrelatorio": self.idrelatorio
        }
