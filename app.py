from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def home():
    candidates = utils.load_candidates_from_json()
    return render_template('home.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def get_candidate_id(id):
    candidate = utils.get_candidate(id)
    return render_template('single.html', candidate=candidate)


if __name__ == '__main__':
    app.run(debug=True)