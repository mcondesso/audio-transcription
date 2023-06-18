# Run the app

- `docker compose up` runs the whole app

Otherwise:
- Run `poetry run flask run` from `backend` folder to run the backend
- Run `source env/bin/activate && python app.py` from `frontend` folder to run the frontend

# TODO:

## Fixes:

- [x] fix backend running with poetry
- [x] refactor backend into Flask app structure with `app.py`, `src/routes` and `src/services`

- [ ] fix frontend running with poetry
- [ ] fix backend running with docker compose
- [ ] fix frontend running with docker compose
- [ ] make sure whole app runs with docker compose

## Nginx


- [ ] add nginx as reverse proxy

## Improve frontend
- [ ] pick a JS framework
