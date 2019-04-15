# Import OS to get environment variables
import os

# Get Flask and associated modules
from flask import Flask, request

# Define the Flask app name from the filename
app = Flask(__name__)

# Get environment
env = os.environ.get('appenv', 'Development')

################
# Begin Routes #
################

# Root
@app.route('/')
def hello_world():
    target = request.args.get('target', 'World')
    return \
        'Hello {}!\n'.format(target) + \
        'This is running in the {} environment on Cloud Run!\n'.format(env)

##############
# End Routes #
##############

# Start development webserver on $PORT (or 8080 if environment variable not set) when file ran directly)
#if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
