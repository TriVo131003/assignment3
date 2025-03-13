from app.models import ExamResult
from app import db
from sqlalchemy.sql import func, case

class ExamResultService:
    @staticmethod
    def get_top_students(limit=10):
        top_students = (
            db.session.query(
                ExamResult.sbd,
                func.coalesce(ExamResult.toan, 0).label("toan"),
                func.coalesce(ExamResult.vat_li, 0).label("vat_li"),
                func.coalesce(ExamResult.hoa_hoc, 0).label("hoa_hoc"),
                (func.coalesce(ExamResult.toan, 0) + 
                 func.coalesce(ExamResult.vat_li, 0) + 
                 func.coalesce(ExamResult.hoa_hoc, 0)).label("total_score")
            )
            .order_by(db.desc("total_score"))
            .limit(limit)
            .all()
        )
        return [
            {"sbd": sbd, "toan": toan, "vat_li": vat_li, "hoa_hoc": hoa_hoc, "total_score": total_score}
            for sbd, toan, vat_li, hoa_hoc, total_score in top_students
        ]

    @staticmethod
    def get_exam_result(sbd):
        exam_result = ExamResult.query.filter_by(sbd=sbd).first()
        if not exam_result:
            return None

        scores = [
            exam_result.toan, exam_result.ngu_van, exam_result.ngoai_ngu,
            exam_result.vat_li, exam_result.hoa_hoc, exam_result.sinh_hoc,
            exam_result.lich_su, exam_result.dia_li, exam_result.gdcd
        ]
        
        valid_scores = [score for score in scores if score is not None] 
        
        average_score = round(sum(valid_scores) / len(valid_scores), 2) if valid_scores else 0.0

        return {
            "sbd": exam_result.sbd,
            "toan": exam_result.toan,
            "ngu_van": exam_result.ngu_van,
            "ngoai_ngu": exam_result.ngoai_ngu,
            "vat_li": exam_result.vat_li,
            "hoa_hoc": exam_result.hoa_hoc,
            "sinh_hoc": exam_result.sinh_hoc,
            "lich_su": exam_result.lich_su,
            "dia_li": exam_result.dia_li,
            "gdcd": exam_result.gdcd,
            "ma_ngoai_ngu": exam_result.ma_ngoai_ngu,
            "average_score": average_score 
        }

    @staticmethod
    def get_score_statistics():
        subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
        score_data = {subject: {"Excellent": 0, "Good": 0, "Average": 0, "Weak": 0} for subject in subjects}

        for subject in subjects:
            query = (
                db.session.query(
                    func.count().label("total"),
                    case((getattr(ExamResult, subject) >= 8, "Excellent"),
                         (getattr(ExamResult, subject) >= 6, "Good"),
                         (getattr(ExamResult, subject) >= 4, "Average"),
                         else_="Weak").label("score_category")
                )
                .group_by("score_category")
                .all()
            )

            for total, category in query:
                score_data[subject][category] = total
        
        return score_data