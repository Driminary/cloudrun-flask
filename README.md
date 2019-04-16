# cr-flask
Flask Application on GCP Cloud Run

Use environment variable **appenv** to describe the environment (Development (default)/Production/Test)

Run the following to test the application:
> gunicorn -e appenv='Local Testing' --bind :8080 --workers 1 --threads 8 core:app
