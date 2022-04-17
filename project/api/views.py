from flask import Blueprint, jsonify, request
from sqlalchemy import exc

from database_singleton import Singleton
from project.api.models import Transporte
from project.api.utils.creation_utils import Utils

transporte_blueprint = Blueprint("transporte", __name__)

db = Singleton().database_connection()
utils = Utils()


@transporte_blueprint.route("/schedule", methods=["POST"])
def create_schedule():
    post_data = request.get_json()

    error_response = {"status": "fail", "message": "Invalid payload."}

    if not post_data:
        return jsonify(error_response), 400

    dataViagem = post_data.get("petid")
    origem = post_data.get("nomePet")
    destino = post_data.get("dataNascimento")
    petid = post_data.get("idusuario")
    cabineid = post_data.get("tipopetid")

    schedule = Transporte(
        dataViagem,
        origem,
        destino,
        petid,
        cabineid
    )

    try:
        db.session.add(schedule)
        db.session.commit()

        response = {"status": "success", "data": {"request": schedule.to_json()}}

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
