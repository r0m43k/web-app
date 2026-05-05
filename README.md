# Local k8s
go:8080
py:5000

```bash
minikube start

minikube image build -t go-app:local go-app
minikube image build -t py-app:local py-app

kubectl apply -f k8s/go-app-deployment.yaml
kubectl apply -f k8s/go-app-service.yaml
kubectl apply -f k8s/py-app-deployment.yaml
kubectl apply -f k8s/py-app-service.yaml
```

# Check
```bash
kubectl get deployments,pods,svc

kubectl run curl-test --image=busybox:1.36 --rm -it --restart=Never -- wget -qO- http://go-app:8080
kubectl run curl-test --image=busybox:1.36 --rm -it --restart=Never -- wget -qO- http://py-app:5000
