from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def procesar_texto():
    data = request.get_json()
    texto_recibido = data.get('texto')
    
    # Aquí puedes agregar la lógica para procesar el texto
    texto_procesado = texto_recibido[::-1]  # Ejemplo: invertir el texto

    return jsonify({'texto': texto_procesado})

if __name__ == '__main__':
    app.run(debug=True)

#POWERSHELL
#$Headers = @{ "Content-Type" = "application/json" }
#$Body = '{"texto":"hola"}'
#Invoke-WebRequest -Uri http://127.0.0.1:5000/procesar -Method POST -Headers $Headers -Body $Body


