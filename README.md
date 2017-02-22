This is boilerplate/skeleton code for a flask application meant for a RESTful API (with http and json)

## Current features:

 * Decent general structure
 * Prod/Dev configuration in the environment
 * Clevercloud structure, deployment ready
 * Rollbar integration
 * Endpoint documented with flask-restplus
 * CORS ready
 * JSON logging on the stdout and logentries
 * Test environment: unittest, nose, coverage
 * Code quality: flake8, radon
 * Convenient Makefile

## Some goals/wanted features:

 * Have the swagger UI on ghpages ?
 * Transition to python 3.6 (at least 3.5)
 * Make it public again

## Installation

This project requires pip and virtualenv.
```bash
make install
```

## Run
```bash
make server
```

## Environment variables

 * `DEBUG: boolean` True will enable debug mode, and display full stack trace and an interactive shell in the browser
 * `SECRET_KEY: String` Secret key of the application, make sure to change it every time you make a new project
 * `LOGENTRIES_TOKEN: String` Token for logentries service, can be left empty when developing locally
 * `APP_NAME: String` Application's name
 * `ENVIRONMENT: String` Application's environment (staging or production)
 * `APP_TOKEN: String` Application's token
 * `ROLLBAR_ACCESS_TOKEN: String` Rollbar's app access token

## Documentation

Endpoints are documented using flask-restplus.
The final json document can be reached [here](http://localhost:5000/spec)

## Tests

 [Nose documentation](http://nose.readthedocs.io/en/latest/plugins/cover.html)

 Simple unit tests run
```bash
make test-unit
```

## Code style, quality and Linting

 * Linting is done using flake8.
 * PEP-8 is followed and asserted using flake8 linter. There is a .flake8 file at the root of app, most IDEs/text editors can use it to determine the preferences.
 * Code can be analyzed and metrics extracted through radon. For a more verbose output, you can un-comment the 'radon raw' command.

 To lint type
```bash
make lint
```

To get metrics type
```bash
make analyze
```


## Logging

We have 2 loggers: `http-logger` and `msg-logger`. Both are using JSON as the output format.

The `http-logger` is only used in the `after_request` callback, to output full HTTP requests and responses on STDOUT. You should not have to use it yourself.

The `msg-logger` is used to send general messages either on STDOUT or logentries if configured (See Environment variables). You can use it the following way:

```python
import logging

logger = logging.getLogger('msg-logger')
logger.info({'user_id': 745, 'retries': 3, 'locked': True})
logger.warn('It can also be a string instead of a dictionnary')
```
