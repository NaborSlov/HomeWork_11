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


@app.route('/search/<candidate_name>')
def search_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    count_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, count_candidates=count_candidates)


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    count_candidates = len(candidates)
    skill_name = skill_name.lower().title()
    return render_template('skill.html', candidates=candidates, count_candidates=count_candidates,
                           skill_name=skill_name)


if __name__ == '__main__':
    app.run(debug=True)
