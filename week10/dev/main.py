# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask
import requests

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def hello():
    payload={"instances":[{"fare": 17.75,"extras": 1.0,"trip_total": 7.45,"payment_type": "Cash"}]}
    url='https://us-central1-ml.googleapis.com/v1/projects/msds434-final/models/TIP_MODEL/versions/v1:predict?access_token=ya29.a0AeTM1ieUF8zyGiBDOHZcOsEyuPP1aiwZmGGC_LgGQYdAidGlJBCzyxRi6rHMIxCtbLInTTOnvZ8MySZBzQFQ-umhtgRlGVdFM0YUGQ_RnZDL_dTEpG3qCkgVBYpejAAe3ZpjWrejrMmUPwqBJ3olFpm1iJtd8AaCgYKAWQSARASFQHWtWOmGNnhuzbY5G09ill587oPTA0165'
    r = requests.post(url, json=payload)
    m = "Payload: "+str(payload)+"\n"+str(r.text)
    return m


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
