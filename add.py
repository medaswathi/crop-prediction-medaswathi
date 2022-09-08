from flask import Flask,render_template,request
import pickle

model=pickle.load(open('model.pkl','rb'))

add=Flask(__name__)

@add.route('/')
def homepage():
    return(render_template('index.html'))

@add.route('/predict',methods=['POST'])
def collectData():
    N=float(request.form['N'])
    P=float(request.form['P'])
    K=float(request.form['K'])
    T=float(request.form['T'])
    H=float(request.form['H'])
    PH=float(request.form['PH'])
    R=float(request.form['R'])
    print(N,P,K,T,H,PH,R)
    result=model.predict([[N,P,K,T,H,PH,R]])
    return(result[0])

if __name__=="__main__":
    add.run(debug=True)   