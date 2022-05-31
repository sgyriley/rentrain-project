from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/search')
def rent():
    return render_template('test.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)
    
