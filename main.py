from flask import Flask, jsonify, request,render_template
import pickle
import numpy as np
import pandas as pd



app = Flask(__name__, template_folder="templates")
model = pickle.load(open("model.pkl", "rb"))
col = pickle.load(open("columns.pkl","rb"))



@app.route("/")
def status():
    return render_template("index.html")



@app.route("/predict_form", methods = ["POST"])

def predict_form():

    data = request.form

    mean_radius = data["mean_radius"]
    print("mean radius = " ,float(mean_radius))

    mean_perimeter = data["mean_perimeter"]
    print("mean perimeter = " , float(mean_perimeter))

    mean_area = data["mean_area"]
    print("mean area = " , float(mean_area))

    mean_concave_points = data["mean_concave_points"]
    print("mean concave points = ",float(mean_concave_points))

    worst_radius = data["worst_radius"]
    print("worst radius = " , float(worst_radius))

    worst_perimeter = data["worst_perimeter"]
    print("worst perimeter = ", float(worst_perimeter))

    worst_area = data["worst_area"]
    print("worst area = " ,float(worst_area))

    worst_concave_points = data["worst_concave_points"]
    print("worst concave points = " ,(float(worst_concave_points)))


    array = np.zeros(len(col))
    print(array)

    array[0] = mean_radius
    array[1] = mean_perimeter
    array[2] = mean_area
    array[3] = mean_concave_points
    array[4] = worst_radius
    array[5] = worst_perimeter
    array[6] = worst_area
    array[7] = worst_concave_points
    
    print(array)



    prediction = model.predict([array])
    prediction = prediction[0]
    print("prediction = ", (prediction))

    # if prediction == 0:
    #     prediction = "Benign"
    #     print("prediction = ", (prediction))

    # else:
    #     prediction = "Malignant"
    #     print("prediction = ", (prediction))


    return render_template('Result.html', data=prediction)
     



@app.route("/predict", methods = ["POST"])
def predict():

    data = request.get_json(force = True)

    mean_radius = data["mean_radius"]
    print("mean radius = " + str(mean_radius))

    mean_perimeter = data["mean_perimeter"]
    print("mean perimeter = " + str(mean_perimeter))

    mean_area = data["mean_area"]
    print("mean area = " + str(mean_area))

    mean_concave_points = data["mean_concave_points"]
    print("mean concave points = " + str(mean_concave_points))

    worst_radius = data["worst_radius"]
    print("worst radius = " + str(worst_radius))

    worst_perimeter = data["worst_perimeter"]
    print("worst perimeter = " + str(worst_perimeter))

    worst_area = data["worst_area"]
    print("worst area = " + str(worst_area))

    worst_concave_points = data["worst_concave_points"]
    print("worst concave points = " + str(worst_concave_points))



    prediction = model.predict([[mean_radius, mean_perimeter, mean_area, mean_concave_points, worst_radius, worst_perimeter, worst_area, worst_concave_points]])
    prediction = prediction[0]
    print("prediction = " + str(prediction))

    if prediction == 0:
        prediction = "Benign"
    else:
        prediction = "Malignant"

    return jsonify({"prediction " : prediction})

if __name__ == "__main__":
      app.run(host='0.0.0.0', port=8080, debug=False)

