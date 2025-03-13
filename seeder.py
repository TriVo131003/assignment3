import csv
from app import db, create_app
from app.models import ExamResult


def load_data():
    app = create_app()
    with app.app_context():
        try:
            with open('data/diem_thi_thpt_2024.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                exam_results = []

                for row in reader:
                    exam_result = ExamResult(
                        sbd=row['sbd'],
                        toan=float(row['toan']) if row['toan'] else None,
                        ngu_van=float(row['ngu_van']) if row['ngu_van'] else None,
                        ngoai_ngu=float(row['ngoai_ngu']) if row['ngoai_ngu'] else None,
                        vat_li=float(row['vat_li']) if row['vat_li'] else None,
                        hoa_hoc=float(row['hoa_hoc']) if row['hoa_hoc'] else None,
                        sinh_hoc=float(row['sinh_hoc']) if row['sinh_hoc'] else None,
                        lich_su=float(row['lich_su']) if row['lich_su'] else None,
                        dia_li=float(row['dia_li']) if row['dia_li'] else None,
                        gdcd=float(row['gdcd']) if row['gdcd'] else None,
                        ma_ngoai_ngu=row['ma_ngoai_ngu']
                    )
                    exam_results.append(exam_result)

                db.session.bulk_save_objects(exam_results)
                db.session.commit()
                print("success")

        except Exception as e:
            print("error")
            db.session.rollback()


if __name__ == '__main__':
    load_data()
