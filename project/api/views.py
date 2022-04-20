from flask import Blueprint, jsonify, request
from sqlalchemy import exc
import sys

from project.api.models import Transporte
from project.api.models import db

transporte_blueprint = Blueprint("transporte", __name__)


@transporte_blueprint.route("/schedule", methods=["POST"])
def create_schedule():
    schedule_data = request.get_json()

    error_response = {"status": "fail", "message": "Invalid payload."}

    if not schedule_data:
        return jsonify(error_response), 400

    nomePet = schedule_data.get("nomePet")
    tipoPet = schedule_data.get("tipoPet")
    dataViagem = schedule_data.get("dataViagem")
    origem = schedule_data.get("origem")
    destino = schedule_data.get("destino")
    usuarioid = schedule_data.get("usuarioid")
    relatorioid = schedule_data.get("relatorioid")

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
