from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def introduction():
    return render_template('introduction.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
