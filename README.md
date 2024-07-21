
## Description

Client API - [Flask](https://flask.palletsprojects.com/en/3.0.x/) + Mongo + Docker.




## Running the app (Docker)

```bash
# build
$ make rebuild

# stop
$ make stop

# start
$ make start

```

## How to test
1. create a .env file at the root of project with atleast the next variables:
   ```
      MONGO_URI = "mongodb://mongodb_client_portfolio:27018/client_portfolios"
      APP_PORT = 5001
   ```
2. Run the app


## License

Nest is [MIT licensed](LICENSE).
