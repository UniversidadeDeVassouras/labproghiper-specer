from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/blog/<newsId>")
def blogDetail(newsId):
    return render_template('blog-details.html')


@app.route("/club")
def club():
    return render_template('club.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internalServerError(e):
    return render_template('500.html'), 500
