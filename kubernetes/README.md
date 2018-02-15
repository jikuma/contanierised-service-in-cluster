# Steps to deploy service to kubernetes

kubectl create -f .\deployment.yml

kubectl create -f .\service.yaml

kubectl get svc

after the public api is exposed navigate to http://<ip>:5000/
