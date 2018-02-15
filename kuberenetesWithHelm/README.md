# Helm command to install the service

helm install --name example --set image.tag=4 .\mychart\ 

helm ls

helm upgrade example --set image.tag=5 .\mychart\


helm rollback example 1
