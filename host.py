from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route("/", methods=['POST'])
def webhook():
        allowed = False
        request_info = request.json
        for x in request_info['request']['object']['spec']['containers']:
                if "nginx" in x['image']:
                        allowed = True
                        break
        admission_response = {
                "allowed": allowed,
                "uid": request_info['request']['uid']
        }
        admissionReview = {
                "apiVersion": "admission.k8s.io/v1",
                "kind": "AdmissionReview",
                "response": admission_response
        }
        return jsonify(admissionReview)
app.run(host="0.0.0.0")