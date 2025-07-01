# Set up for Grafana Prometheus stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus-stack prometheus-community/kube-prometheus-stack --namespace=monitoring --create-namespace
# create values.yaml if required... then 
helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring --values values.yaml
k apply -f loadbalancer.yaml
```
