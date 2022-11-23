#import Flask 
from flask import Flask, render_template, request

#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #get form data
        f1 = request.form.get('f1')
        f2 = request.form.get('f2')
        f3 = request.form.get('f3')
        return render_template('predict.html')
    pass
