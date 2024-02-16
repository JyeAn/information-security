# Web - K8s Version with ingress and CSR in Minikube

[web_0927.tar.gz](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a836fb69-f895-43f5-bd87-5b4914b40b49/web_0927.tar.gz)

- **Minikube K8s**
    
    > Enable Ingress
    > 
    > 
    > `minikube addons enable ingress`
    > 
    > Check pods of ingress-nginx
    > 
    > `kubectl get pods --namespace=ingress-nginx`
    > 
    > ```bash
    > NAME                                        READY   STATUS      RESTARTS   AGE
    > ingress-nginx-admission-create-94n6h        0/1     Completed   0          21h
    > ingress-nginx-admission-patch-2clch         0/1     Completed   1          21h
    > ingress-nginx-controller-5959f988fd-nj94x   1/1     Running     0          21h
    > ```
    > 
    > ---
    > 
    > Ingress Controller
    > 
    > [Installation Guide - NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/)
    > 
    > ---
    > 
- **Keycloak**
    
    > Pull image
    > 
    > 
    > `minikube image pull [quay.io/keycloak/keycloak:18.0.0](http://quay.io/keycloak/keycloak:18.0.0)`
    > Deployment & Service
    > 
    > - `kubectl create -f https://gitlab.com/kennythecat/k8s-project/-/raw/main/minikube/keycloak.yaml`
    >     
    >     ```yaml
    >     apiVersion: v1
    >     kind: Service
    >     metadata:
    >       name: keycloak
    >       labels:
    >         app: keycloak
    >     spec:
    >       ports:
    >       - name: http
    >         port: 80
    >         targetPort: 8080
    >       selector:
    >         app: keycloak
    >       type: LoadBalancer
    >     ---
    >     apiVersion: apps/v1
    >     kind: Deployment
    >     metadata:
    >       name: keycloak
    >       labels:
    >         app: keycloak
    >     spec:
    >       replicas: 1
    >       selector:
    >         matchLabels:
    >           app: keycloak
    >       template:
    >         metadata:
    >           labels:
    >             app: keycloak
    >         spec:
    >           containers:
    >           - name: keycloak
    >             image: quay.io/keycloak/keycloak:18.0.0
    >             args: ["start-dev"]
    >             env:
    >             - name: KEYCLOAK_ADMIN
    >               value: "admin"
    >             - name: KEYCLOAK_ADMIN_PASSWORD
    >               value: "admin"
    >             - name: KC_PROXY
    >               value: "edge"
    >             ports:
    >             - name: http
    >               containerPort: 8080
    >             readinessProbe:
    >               httpGet:
    >                 path: /realms/master
    >                 port: 8080
    >     ```
    >     
    > 
    > Ingress
    > 
    > - `kubectl create -f https://gitlab.com/kennythecat/k8s-project/-/raw/main/minikube/ingress.yaml`
    >     
    >     ```yaml
    >     apiVersion: networking.k8s.io/v1
    >     kind: Ingress
    >     metadata:
    >       name: keycloak
    >       annotations:
    >         nginx.ingress.kubernetes.io/rewrite-target: /
    >         nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
    >     spec:
    >       rules:
    >       - http:
    >           paths:
    >           - path: /
    >             pathType: Prefix
    >             backend:
    >               service:
    >                 name: keycloak
    >                 port:
    >                   number: 80
    >     ```
    >     
    > 
    > ---
    > 
- **Nginx**
    
    > Install Nginx
    > 
    > 
    > ```bash
    > sudo apt-get update
    > sudo apt-get install nginx
    > ```
    > 
    > - /etc/nginx/sites-aviliable/default
    >     
    >     ```bash
    >     server {
    >             listen 443 ssl;
    >             listen [::]:443 ssl default_server;
    >     
    >             server_name test2.ntut-smodist.tw;
    >     
    >             ssl_certificate     /etc/ssl/certs/fullchain.pem;
    >             ssl_certificate_key /etc/ssl/certs/private.key;
    >             ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
    >             ssl_ciphers         HIGH:!aNULL:!MD5;
    >     
    >             location / {
    >                     proxy_pass    https://test2.ntut-smodist.tw;
    >     
    >                     proxy_set_header X-Real-IP $remote_addr;
    >                     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    >                     proxy_set_header X-Forwarded-Proto $http_x_forwarded_proto;
    >     
    >                     proxy_buffer_size   128k;
    >                     proxy_buffers   4 256k;
    >                     proxy_busy_buffers_size   256k;
    >             }
    >     ```
    >     
    >     <aside>
    >     💡 The Yellow background text shoud follow your own path!
    >     
    >     </aside>
    >     
    > 
    > Start
    > 
    > `sudo systemctl start nginx`
    > 
    > Stop
    > 
    > `sudo systemctl stop nginx`
    > 
    > Restart
    > 
    > `sudo systemctl start nginx`
    > 
    > Uninstall
    > 
    > ```bash
    > sudo apt-get remove nginx nginx-common
    > sudo apt-get purge nginx nginx-common
    > sudo apt-get autoremove
    > ```
    > 
    > ---
    > 
    > Source
    > 
    > [完全移除, 安裝,重啟nginx](http://www.cclin.xyz/2015/07/nginx.html)
    > 
    > Nginx Command:
    >