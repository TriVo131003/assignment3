from flask import Blueprint, request, jsonify, render_template
from app.models import ExamResult
from app import db
from app.service import ExamResultService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/leader-board', methods=['GET'])
def leaderboard():
    results = ExamResultService.get_top_students()
    if request.args.get("format") == "json":
        return jsonify(results)
    return render_template("leader-board.html", results=results)

@main_bp.route('/search-score', methods=['POST', 'GET'])
def check_score():
    sbd = request.form.get('sbd') if request.method == 'POST' else request.args.get('sbd')
    error = None
    result = None

    if sbd:
        result = ExamResultService.get_exam_result(sbd)
        if not result:
            error = "No results found."
    elif request.method == 'POST':
        error = "Please provide a valid registration number."

    return render_template('search-score.html', result=result, error=error)

@main_bp.route('/report', methods=['GET'])
def score_statistics():
    score_data = ExamResultService.get_score_statistics()
    return render_template('report.html', score_data=score_data)