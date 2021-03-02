from flask import Flask,render_template,request
from pythonFile import *
import pyttsx3
app=Flask(__name__)   
@app.route('/result', methods=["POST","GET"])
def index():
	word = ""
	outPut = ""
	if request.method=="POST":
		d=request.form
		file1 = open("pythonFile.py", "w")
		word=d["code"]
		if d["buttonName"] == "Get ready to complie":
			buttonName = "Show outPut"
		file1.write(word)
		file1.close()
		outPut = startCode()
		return render_template("testPage.html", word = word, outPut = outPut, buttonName = buttonName)
	return render_template("testPage.html", word = word, outPut = outPut, buttonName = "Get ready to complie")
if __name__ == '__main__':
	app.run(debug=True, threaded=True)