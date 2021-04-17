import random
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following


def ma():
    
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def guess():
    try: 
        num
    except NameError:
        num = random.randint(1,100)
        
    print(request.form)
    guessedNum= request.form['guessedNum']
    guessedNum = int(guessedNum)
    if(guessedNum > num):
        return render_template("high.html")
    elif(guessedNum < num):
        return render_template("low.html")
    else:
        return render_template("win.html")

def reset():
    del num

if __name__=="__main__":    
    app.run(debug=True)    

