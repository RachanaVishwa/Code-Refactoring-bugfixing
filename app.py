from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/home', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        note = request.form['note']
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)