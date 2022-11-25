import requests
r = requests.post("https://us-central1-ml.googleapis.com/v1/projects/msds434-final/models/TIP_MODEL/versions/v1:predict?access_token=ya29.a0AeTM1icVPM2w1ra3i4QokHaQPzjEw9jljFZFHOtr-qj4txNtYuM_syjYPKRZq6UVat-_XU_28ibFjBtsUvd_iO2jD5NUL3jcIS078kPby4KDlHp-ahPkB7JcBAQ1Ukc4GaNQq272aRJjmMyjJnFPI0o0tXNcVwaCgYKAaUSARASFQHWtWOmLIe4jHu-Rak4ZmtTMV_9eQ0165", data={"instances": [{"fare": 17.75,"extras": 1.0,"trip_total": 7.45,"payment_type": "Cash"}]})
print(r.status_code, r.reason)
