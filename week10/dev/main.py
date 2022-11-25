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
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("https://httpbin.org/post", data=payload)
    #self.response.headers['Content-Type'] = 'json'
    self.response.out.write(r.text)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
