from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import uuid

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"
    usuarioid = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
            "usuarioid": self.usuarioid,
            "nomeCompleto": self.nomeCompleto,
            "cpf": self.cpf
        }


class Raca(db.Model):
    __tablename__ = "raca"
    racaid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raca = db.Column(db.Text, nullable=False)

    def __init__(
            self,
            raca
    ):
        self.raca = raca

    def to_json(self):
        return {
            "racaid": self.racaid,
            "raca": self.raca
        }


class TipoPet(db.Model):
    __tablename__ = "tipopet"
    tipopetid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipoPet = db.Column(db.Enum('CACHORRO', 'GATO'), nullable=False)

    def __init__(
            self,
            tipoPet
    ):
        self.tipoPet = tipoPet

    def to_json(self):
        return {
            "tipopetid": self.tipopetid,
            "tipoPet": self.tipoPet
        }


class Pet(db.Model):
    __tablename__ = "pet"
    petid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dataNascimento = db.Column(db.Date, nullable=False)
    nomePet = db.Column(db.Text, nullable=False)
    idusuario = db.Column(db.SmallInteger, db.ForeignKey("usuario.usuarioid"))
    tipopetid = db.Column(db.SmallInteger, db.ForeignKey("tipopet.tipopet"))
    racaid = db.Column(db.SmallInteger, db.ForeignKey("raca.racaid"))

    def __init__(
            self,
            dataNascimento,
            nomePet,
            idusuario,
            tipopetid,
            racaid
    ):
        self.dataNascimento = dataNascimento
        self.nomePet = nomePet
        self.idusuario = idusuario
        self.tipopetid = tipopetid
        self.racaid = racaid

    def to_json(self):
        return {
            "petid": self.petid,
            "nomePet": self.nomePet,
            "dataNascimento": self.dataNascimento,
            "idusuario": self.idusuario,
            "tipopetid": self.tipopetid,
            "racaid": self.racaid
        }


class Cabine(db.Model):
    __tablename__ = "cabine"
    cabineid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qrCabine = db.Column(db.Text, nullable=False)

    def __init__(
            self,
            qrCabine
    ):
        self.qrCabine = qrCabine

    def to_json(self):
        return {
            "cabineid": self.cabineid,
            "qrCabine": self.qrCabine
        }


class Relatorio(db.Model):
    __tablename__ = "relatorio"
    relatorioid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dadosRelatorio = db.Column(postgresql.JSON)

    def __init__(
            self,
            dadosRelatorio
    ):
        self.dadosRelatorio = dadosRelatorio

    def to_json(self):
        return {
            "relatorioid": self.relatorioid,
            "dadosRelatorio": self.dadosRelatorio
        }


class Transporte(db.Model):
    __tablename__ = "transporte"

    transporteid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomePet = db.Column(db.Text, nullable=False)
    tipoPet = db.Column(db.Enum('CACHORRO', 'GATO'), nullable=False)
    dataViagem = db.Column(db.Date, nullable=False)
    origem = db.Column(db.Text, nullable=False)
    destino = db.Column(db.Text, nullable=False)
    usuarioid = db.Column(db.Integer, db.ForeignKey("usuario.usuarioid"))
    relatorioid = db.Column(db.Integer, db.ForeignKey("usuario.usuarioid"))

    def __init__(
            self,
            nomePet,
            tipoPet,
            dataViagem,
            origem,
            destino,
            usuarioid,
            relatorioid
    ):
        self.nomePet = nomePet
        self.tipoPet = tipoPet
        self.dataViagem = dataViagem
        self.origem = origem
        self.destino = destino
        self.usuarioid = usuarioid
        self.relatorioid = relatorioid

    def to_json(self):
        return {
            "transporteid": self.transporteid,
            "nomePet": self.nomePet,
            "tipoPet": self.tipoPet,
            "dataViagem": self.dataViagem,
            "origem": self.origem,
            "destino": self.destino,
            "usuarioid": self.usuarioid,
            "relatorioid": self.relatorioid
        }
