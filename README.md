# RAM Usage Task

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-green.svg)](https://shields.io/)

This repository contains a task for HPDS company.

## Usage

The backend can be started using the following command.

```bash
python services/backend.py
```

The FastAPI service can start using the following command.

```bash
uvicorn services.api:app --host 0.0.0.0 --port 8080
```

They can also run in parallel using the following command.

```bash
. run.sh
```

## Project layout

The code for both backend and api is contained in the `service` folder. All of the test are in the `tests` folder. 

```text
├── service       <- folder for backend and api
│   ├── backend.py   <- code for adding memory info to database every 1 minute
│   └── api.py       <- code for the FastAPI only route (/ram/{n})
├── utils         <- common code throughout the project
│   ├── db_connect.py   <- code for connecting to database and querying
│   └── jsonify.py      <- code for json formatting the database output
│   └── logger.py       <- code for using logging through the project
└── tests         <- folder for all of the tests
    ├── test_api.py           <- test api route
    └── test_backend.py       <- test backend
```

## Data Model

The RAM model contains the following fields:

| Name        | Type     | Optional |
|-------------|----------|----------|
| id          | Integer  | False    |
| created_at  | Datetime | False    |
| total       | Real     | True     |
| free        | Real     | True     |
| used        | Real     | True     |


## Docker

The image can be built and then run using the following commands.

```bash
docker build -t app .
docker run -p 8080:8080 app
```

## Author

[Mahsa Fathi](https://www.linkedin.com/in/mahsa-fathi-68216112b/)

## License

Licensed under the Apache License. See [LICENSE](LICENSE)
