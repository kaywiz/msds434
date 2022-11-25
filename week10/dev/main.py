import requests
r = requests.post("https://us-central1-ml.googleapis.com/v1/projects/msds434-final/models/TIP_MODEL/versions/v1:predict?access_token=ya29.a0AeTM1ieYEv4ctIelG7538Q7xcxl4Dmj7JtTF110rB5bzvSud0ojaNPyQybjFBzvt19RR3etbs0fiKt9AgDduhEqf9XcReZlJCQT7LNsgi1rYaNDBIZdtQ_tP_ZjyRRnUVf5LX3RMBhQSk5R9Uds2QICcKJFlaCgYKAWESARASFQHWtWOmEKtKS9KF5-bU7-vRQomksw0163", data={"instances": [{"fare": 17.75,"extras": 1.0,"trip_total": 7.45,"payment_type": "Cash"}]})
print(r.status_code, r.reason)
