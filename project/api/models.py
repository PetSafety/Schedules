from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import uuid

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"
    usuarioid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
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
    racaid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
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
    tipopetid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
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
    petid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
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
    cabineid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
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


class Transporte(db.Model):
    __tablename__ = "transporte"

    transporteid = db.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    dataViagem = db.Column(db.Date, nullable=False)
    origem = db.Column(db.Text, nullable=False)
    destino = db.Column(db.Text, nullable=False)
    petid = db.Column(db.SmallInteger, db.ForeignKey("pet.petid"))
    cabineid = db.Column(db.SmallInteger, db.ForeignKey("cabine.cabineid"))

    def __init__(
            self,
            dataViagem,
            origem,
            destino,
            petid,
            cabineid
    ):
        self.dataViagem = dataViagem,
        self.origem = origem,
        self.destino = destino,
        self.petid = petid,
        self.cabineid = cabineid

    def to_json(self):
        return {
            "transporteid": self.transporteid,
            "dataViagem": self.dataViagem,
            "origem": self.origem,
            "destino": self.destino,
            "petid": self.petid,
            "cabineid": self.cabineid
        }
