from flask import Blueprint, request, jsonify, render_template
from app.models import ExamResult
from app import db
from app.service import ExamResultService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/leader-board')
def leaderboard():
    results = ExamResultService.get_top_students()
    if request.args.get("format") == "json":
        return jsonify(results)
    return render_template("leader-board.html", results=results)

@main_bp.route('/search-score', methods=['GET', 'POST'])
def check_score():
    sbd = request.values.get('sbd')  
    result = ExamResultService.get_exam_result(sbd) if sbd else None
    error = "No results found for the given registration number." if sbd and not result else None
    
    if request.method == 'POST' and not sbd:
        error = "Please provide a valid registration number."
    
    return render_template('search-score.html', result=result, error=error)

@main_bp.route('/report')
def score_statistics():
    score_data = ExamResultService.get_score_statistics()
    return render_template('report.html', score_data=score_data)