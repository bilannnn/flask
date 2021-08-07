from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Ivan',
        'title': 'Blog Post 1',
        'content': 'Blog content',
        'date_posted': '09 08 2021'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=7777)
