# psycopg-operational-error

## Instructions:

First, make sure to either activate Docker Desktop or have Docker installed on your machine (https://docs.docker.com/get-docker/). Then, follow the instructions below:

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Host a PostgreSQL database on your local machine. You can use the following command to host a PostgreSQL database using Docker:
```bash
docker compose up
```

3. Run the script:
```bash
python main.py
```

## Output:

The script will output the following:

```
Database not connected successfully: connection to server at "localhost" (127.0.0.1), port 5432 failed: fe_sendauth: no password supplied
```