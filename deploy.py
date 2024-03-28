from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
#load the model 
model=pickle.load(open('saved_model.sav','rb'))

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        # Get user input
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Make prediction
        
        predicted_species =model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
        
        return render_template('result.html', predicted_species=predicted_species)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
def home():
    result=''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    # Get user input
    sepal_length=float(request.form['sepal_length'])
    sepal_width=float(request.form['sepal_width'])
    petal_length=float(request.form['petal_length'])
    petal_width=float(request.form['petal_width'])
    
    # Make Prediction
    result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    return render_template('index.html',**locals())

if __name__=='__main__':
    app.run(debug=True)
'''
