# Copyright 2016 Google Inc. All rights reserved.
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

"""
Sample application that demonstrates different ways of fetching
URLS on App Engine
"""

import logging
import urllib

# [START urllib2-imports]
import urllib2
# [END urllib2-imports]

# [START urlfetch-imports]
from google.appengine.api import urlfetch
# [END urlfetch-imports]
import webapp2

try:
    form_data = urllib.urlencode(UrlPostHandler.form_fields)
    instances = {"instances": [{"fare": 17.75,"extras": 1.0,"trip_total": 7.45,"payment_type": "Cash"}]}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    result = urlfetch.fetch(
        url='https://us-central1-ml.googleapis.com/v1/projects/msds434-final/models/TIP_MODEL/versions/v1:predict?access_token=ya29.a0AeTM1ieYEv4ctIelG7538Q7xcxl4Dmj7JtTF110rB5bzvSud0ojaNPyQybjFBzvt19RR3etbs0fiKt9AgDduhEqf9XcReZlJCQT7LNsgi1rYaNDBIZdtQ_tP_ZjyRRnUVf5LX3RMBhQSk5R9Uds2QICcKJFlaCgYKAWESARASFQHWtWOmEKtKS9KF5-bU7-vRQomksw0163',
        payload=instances,
        method=urlfetch.POST,
        headers=headers)
    self.response.write(result.content)
except urlfetch.Error:
    logging.exception('Caught exception fetching url')
