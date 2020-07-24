1. Create app.py file
2. Create requirements.txt file
3. Create and push docker image 
docker build -t pkw0301/app:1.0 .
docker login
docker push pkw0301/app:1.0

4. Create manifest file for blue environments
vi blue-1.yml
5. Create service manifest file for blue deployment
vi service-1.yaml

6. Deploy blue environment manifest file
kubectl apply -f blue-1.yml
kubectl get deployments
kubectl get pods

7. Create services for blue enviroments
kubectl apply -f service-1.yaml
kubectl get svc

access from browser: http://<K8s Master IP>:<NodePort Port>/ping


8. Now Let’s change in the code (consider new feature)
in our app.py file, change the response from: Hi, This code is develop by Prakash Kumar: 1
to Hi, This code is develop by Prakash Kumar: 2

9. Now it’s time to build docker image with new tag
docker build -t pkw0301/app:2.0 .
docker login
docker push pkw0301/app:2.0

10. Create manifest file for Green environments
vi green-2.yml

11. Deploy Green environment manifest file
kubectl apply -f green-2.yml --force
kubectl get deployments
kubectl get pods



12. In order to point to Green Environment update service manifest file and update version from 1.0 to 2.0
kubectl apply -f service-1.yaml

13. Reload application URL, now it should point to Green environment.
14. If there is a new change your can repeat the process.
Done!!!
