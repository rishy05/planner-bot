from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import os
import shutil
import json
from plan import get_plan
from image_search import get_image

app = Flask(__name__)

cors = CORS(app)


# T add <Origin city> <Destination city> <Number of People> <Number of days>
@app.route("/plan", methods=["POST"])
def plan_gen():

    origin = request.form.get("origin")
    desti = request.form.get("desti")
    num_peo = request.form.get("num_peo")
    num_days = request.form.get("num_days")

    result = get_plan(origin, desti, num_peo, num_days)

    print(result)

    return jsonify({"message": f"{result[0]}", "places": result[1]})


@app.route("/places", methods=["POST"])
def get_places_img():
    place_names = request.form.get("place")
    print(place_names)
    l = get_image(place_names.split(","))

    return jsonify({"images": l})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
