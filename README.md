- Ensure you have: Docker Desktop, Docker

- Clone the Repository

git clone https://github.com/TriVo131003/assignment3.git

- Environment variables

you can update database_url in both config.py and docker-compose.yml

- Running the project

docker-compose up --build

- Seeder

The application automatically loads data. However, if data already exists in the ExamResult model, the seeder will not function.

- Viewing the web: http://localhost:5000/

- Stopping project

docker-compose down

- Demo link

- Deployment site: https://assignment3-gxu1.onrender.com/
