import requests

resp = requests.post("https://getmnist-gzia42tk5q-ts.a.run.app", files={'file': open('D://Jupyter//GCP Deploy//google-cloud-run//test//three.png', 'rb')})

print(resp.json())
