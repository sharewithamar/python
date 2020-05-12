from flask import Flask, render_template
app = Flask(__name__)
print(__name__)
print()


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    # return 'Hello, Amar- Learning python web dev!  cool'
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/about.html')
def about():
    # return 'Hello, Amar- Learning python web dev!  cool'
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'Amar thoughts - yoda stoic'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog devil'
