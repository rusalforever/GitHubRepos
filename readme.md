postgres=# CREATE DATABASE dbrepos;
postgres=# CREATE USER reposuser WITH PASSWORD 'reposuser password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbrepos TO reposuser;




WEB:
http://127.0.0.1:8000/

API:
http://127.0.0.1:8000/api/repos/:id/
http://127.0.0.1:8000/api/repos/:id/