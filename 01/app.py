from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name': 'Lee Wee Giak',
        'age': 18,
        'sex': 'Men',
        'city': 'Kuching',
        'Country': 'Malaysia'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()