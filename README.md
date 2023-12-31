# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

You will need to create a Trello account and generate and API Key and Token. Follow the instructions in the below links:
    [https://trello.com/signup]
    [https://trello.com/app-key]

Once you have an account, create some cards (at least one in To Do list.)

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Set the following value in the `'.env` file once you have got these from Trello.
    [API_KEY=]
    [API_TOKEN=]

To get the Board Id:
```bash
    * Go to your Trello Board
    * Add ".json" to the end of the URL
    * Format the JSON so it is readable, search for idBoard OR
    * the first value is normally the id {"id":"....
```
    [BOARD_ID=]

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

You will be able to see:
```bash
 * All your tasks
 * If you want to move a task to Done hit the Complete button
 * Add new tasks to a list you have available on Trello board i.e. To Do, Doing, Done.
``` 

## Testing

To run all tests configured, where files are test_*py or *_test.py do so by running:
```bash
$ poetry run pytest
```

You should see either all tests PASSED or some FAILED:
```bash
 * ====================================================================================================================== short test summary info====================================================================================================================== 
 * FAILED todo_app/test_view_model.py::test_view_model_to_do_items - AssertionError: assert 'Done' == 'To Do'
 * ==================================================================================================================== 1 failed, 1 passed in 9.24s===================================================================================================================
```

