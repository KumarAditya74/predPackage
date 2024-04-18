from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/predict', methods = ['POST', "GET"])

def predict_datapoint(): 
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        data = CustomData(
            dsa = int(request.form.get('dsa')),
            cgpa = float(request.form.get('cgpa')),
            Kml = request.form.get("Kml"), 
            Kdsa= request.form.get("Kdsa"), 
            Kpython = request.form.get("Kpython"),
            KJavascript = request.form.get("KJavascript"), 
            club = request.form.get("club"), 
            backlogs = int(request.form.get("backlogs")) 
            
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0],2)

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)
#http://127.0.0.1:5000/
# in browser