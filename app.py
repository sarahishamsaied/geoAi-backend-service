from flask import Flask, request, jsonify
from gradio_client import Client

client = Client(
    "https://ibm-nasa-geospatial-prithvi-100m-sen1floods11-demo.hf.space/")

app = flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the file URL and other parameters from the request
    file_url = request.form.get('file_url')
    parameter_5_value = request.form.get('parameter_5_value')

    # Use the Gradio client to make predictions
    result = client.predict(
        file_url,
        fn_index=0
    )

    # Return the prediction result as JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
