from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from project.api.models import Transporte, Usuario, Pet
from project.api.models import db

transporte_blueprint = Blueprint("transporte", __name__)


@transporte_blueprint.route("/schedule", methods=["POST"])
def create_schedule():
    post_data = request.get_json()

    error_response = {"status": "fail", "message": "Invalid payload."}

    if not post_data:
        return jsonify(error_response), 400

    nomePet = post_data("nomePet")
    tipoPet = post_data("tipoPet")
    dataViagem = post_data("dataViagem")
    origem = post_data("origem")
    destino = post_data("destino")
    usuarioid = post_data("usuarioid")
    relatorioid = post_data("relatorioid")

    transporte = Transporte(    
        nomePet,
        tipoPet,
        dataViagem,
        origem,
        destino,
        usuarioid,
        relatorioid
    )

    try:
        db.session.add(transporte)
        db.session.commit()

        response = {"status": "success", "data": {"request": transporte.to_json()}}

        return jsonify(response), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(error_response), 400


@transporte_blueprint.route("/schedule", methods=["GET"])
def get_all_schedule():
    response = {
        "status": "success",
        "data": {
            "schedules": [schedule.to_json() for schedule in Transporte.query.all()]
        },
    }
    return jsonify(response), 200
