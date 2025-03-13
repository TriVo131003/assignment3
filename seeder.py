from app import db, create_app

def load_data():
    app = create_app()
    with app.app_context():
        try:
            conn = db.engine.raw_connection()
            cursor = conn.cursor()
            
            with open('data/diem_thi_thpt_2024.csv', 'r', encoding='utf-8') as file:
                next(file) 
                cursor.copy_expert(
                    "COPY score(sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu) FROM STDIN WITH CSV NULL ''",
                    file
                )
            
            conn.commit()
            cursor.close()
            conn.close()
            print("Data import successful.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    load_data()
