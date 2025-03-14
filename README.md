- Ensure you have: Docker Desktop, Docker

- Clone the Repository

git clone https://github.com/TriVo131003/assignment3.git

- Environment variables

you can change database_url in config.py and docker-compose.yml

- Running project

docker-compose up

- Running seeder.py

docker exec -it python_intern python seeder.py

- View web

http://localhost:5000/

- Stopping project

docker-compose down
