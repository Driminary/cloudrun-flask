# cr-flask
Flask Application on GCP Cloud Run

Use environment variable **appenv** to describe the environment (Development (default)/Production/Test)

Run the following to test the application:
> gunicorn -e appenv='Local Testing' --bind :8080 --workers 1 --threads 8 core:app

To run the docker image locally (using a GCR image and replicating the Cloud Run environment PORT variable), use:
> PORT=8080 && docker run -p 8080:${PORT} -e PORT=${PORT} -e appenv='Local Test' gcr.io/**{PROJECT}**/cr-flask-dev
