from flask import Flask, request, jsonify

server = Flask(__name__)

@server.route('/')
def home():
    return "¡Hola, mundo!"

@server.route('/WebHookTest', methods=['POST'])
def ProcesarJson():
    if request.is_json:
        data = request.get_json()
        response = {
            "mensaje": data,
            #"Body": data['Body']
        }
 
        return jsonify(response), 200
    else:
        return jsonify({"mensaje": "La solicitud no contiene un JSON válido"}), 400
 
if __name__ == '__main__':
    server.run(debug=True)