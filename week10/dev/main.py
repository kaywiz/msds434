print(r.status_code, r.reason)


# Copyright 2015 Google Inc. All Rights Reserved.
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

# [START gae_flex_quickstart]
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
class MainPage(webapp.RequestHandler):
  def get(self):
    r = requests.post("https://us-central1-ml.googleapis.com/v1/projects/msds434-final/models/TIP_MODEL/versions/v1:predict?access_token=ya29.a0AeTM1icVPM2w1ra3i4QokHaQPzjEw9jljFZFHOtr-qj4txNtYuM_syjYPKRZq6UVat-_XU_28ibFjBtsUvd_iO2jD5NUL3jcIS078kPby4KDlHp-ahPkB7JcBAQ1Ukc4GaNQq272aRJjmMyjJnFPI0o0tXNcVwaCgYKAaUSARASFQHWtWOmLIe4jHu-Rak4ZmtTMV_9eQ0165", data={"instances": [{"fare": 17.75,"extras": 1.0,"trip_total": 7.45,"payment_type": "Cash"}]})
    self.response.headers['Content-Type'] = 'json'
    self.response.out.write(r.status_code)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
