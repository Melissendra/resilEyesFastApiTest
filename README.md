# resilEyesFastApiTest

## Installation
- Go inside the directory in which you want to install the application:
  - `git clone git@github.com:Melissendra/resilEyesFastApiTest.git`
  - `cd resilEyesFastApiTest`

### Create your python environment:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`

## Launch the application
- `uvicorn app.main:app`

## Endpoints
- Users list and create user:
    - http://127.0.0.1:8000/users/
- Get one user by id, update him or delete him (only the http call change: get, put or delete):
    - http://127.0.0.1:8000/users/{user_id} -> example: http://127.0.0.1:8000/users/1
- Swagger FastAPI:
    - http://127.0.0.1:8000/docs