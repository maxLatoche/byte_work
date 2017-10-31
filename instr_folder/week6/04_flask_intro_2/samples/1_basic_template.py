from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def raw_template():
    return render_template('1_basic_sample.html', name='Scarlett Johansson')

if __name__ == "__main__":
    app.run(debug=True)
