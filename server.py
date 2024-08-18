from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Get the directory where the script is located
project_directory = os.path.dirname(os.path.abspath(__file__))
results_file_path = os.path.join(project_directory, 'results.txt')

# Debug print to check the path
print(f"Saving results to: {results_file_path}")

@app.route('/save-result', methods=['POST'])
def save_result():
    data = request.json
    with open(results_file_path, 'a') as f:
        f.write(f"Name: {data['name']}, Score: {data['score']}, Incorrect: {data['incorrect']}\n")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
