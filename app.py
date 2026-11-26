from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

COLIS = {
        "GT-1001": {"client": "SOTELGAB", "statut": "En transit", "ville": "Libreville", "poids_kg": 120},
    "GT-1002": {"client": "TRANSGABON FRET", "statut": "Livré", "ville": "Port-Gentil"},
}


@app.route("/health")
def health():
    return jsonify(status="ok", service="gabotrans-suivi")


@app.route("/colis/<ref>")
def get_colis(ref):
    colis = COLIS.get(ref)
    if colis is None:
        return jsonify(erreur="Colis introuvable", reference=ref), 404
    return jsonify(reference=ref, **colis)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
