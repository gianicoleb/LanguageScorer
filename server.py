from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Get the directory where the script is located
project_directory = os.path.dirname(os.path.abspath(__file__))
results_file_path = os.path.join(project_directory, 'results.txt')

# Debug print to confirm the path where results will be saved
print(f"Saving results to: {results_file_path}")

@app.route('/save-result', methods=['POST'])
def save_result():
    data = request.json
    
    # Ensure data contains the expected keys
    if 'name' in data and 'score' in data and 'incorrect' in data:
        # Save the result to the results.txt file
        with open(results_file_path, 'a') as f:
            f.write(f"Name: {data['name']}, Score: {data['score']}, Incorrect: {', '.join(data['incorrect'])}\n")
        
        # Return a success response
        return jsonify({"status": "success"}), 200
    else:
        # Return an error response if expected data is missing
        return jsonify({"status": "error", "message": "Invalid data format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
