import threading
import time
from flask import current_app

class BackgroundTask:
    def __init__(self, interval=600):
        self.interval = interval 
        self.running = False  
        self.thread = threading.Thread(target=self.run, daemon=True) 

    def start(self, app):
        if not self.running:
            self.running = True
            self.app = app
            self.thread.start()

    def stop(self):
        self.running = False

    def run(self):
        with self.app.app_context(): 
            from app.service import ExamResultService 

            while self.running:
                ExamResultService.get_top_students()
                ExamResultService.get_score_statistics()
                time.sleep(self.interval)  

background_task = BackgroundTask()
