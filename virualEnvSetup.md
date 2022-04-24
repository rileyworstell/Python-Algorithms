

python3 -m venv my_env

To activate the environment, run:
    - source my_env/bin/activate

Now that your env is setup you can install whatever modules you need. 

To get out of the env you use the following command
    - exit


## Docker
start with creating dir:
    - mkdir flask_web

"""
From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world:
    return 'hey, flask in docker'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
"""

Now we setup a requirement.txt file:
    - Flask==2.0.2


dockerfile:
"""

"""

Now that we have a Dockerfile, lets build it:
    - docker build --tag python-docker


- docker run --publish 5000:5000 python-docker
then run:
    - docker run --publish 5000:5000 python-docker

