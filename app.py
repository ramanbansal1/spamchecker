from flask import Flask, request, render_template
import joblib


app = Flask(__name__)

@app.route("/")
def home():
	if "message" in request.args:
		message = request.args["message"]
		result = predict(message)
		return render_template("index.html", result=result, message=message)
	return render_template("index.html", result=None)
	
	
def predict(x):
	vectorizer = joblib.load("vectorizer.sav")
	model = joblib.load("model.sav")
	x = vectorizer.transform([x])
	return model.predict(x)[0]

if __name__=="__main__":
  app.run(debug=True)