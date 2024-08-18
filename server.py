from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save-result', methods=['POST'])
def save_result():
    data = request.json
    with open('results.txt', 'a') as f:
        f.write(f"Name: {data['name']}, Score: {data['score']}, Incorrect: {data['incorrect']}\n")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
