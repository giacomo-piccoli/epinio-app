This Aplication is just a Area calculator

Preparing the enviroment for the aplication
For this aplication is recomended to use Minikube, so if you dont have install following the Oficial Doc:https://minikube.sigs.k8s.io/docs/start/

after installing, continue with the steps bellow
```
$ minikube start --driver=docker
```

```
$ minikube addons enable metallb
```

```
$ minikube addons configure metallb

-- Enter Load Balancer Start IP: 192.168.49.100
-- Enter Load Balancer End IP: 192.168.49.120
     Using image metallb/speaker:v0.9.6
     Using image metallb/controller:v0.9.6
  metallb was successfully configured
```

Install epinio on minikube

Epinio need two resources to works, first: one _ingress-control_ and one _cert-manager_.

  In order to install _ingress-control_ use:

```
$ minikube addons enable ingress
```
Cert Manager

to install the cert manager run the commands bellow
```
$ kubectl create namespace cert-manager
$ helm repo add jetstack https://charts.jetstack.io
$ helm repo update
$ helm install cert-manager --namespace cert-manager jetstack/cert-manager \
        --set installCRDs=true \
        --set extraArgs={--enable-certificate-owner-ref=true}
```
After you finish prepraing the enviroment procede with the steps below

first add the helm repo in your machine.
$ helm repo add epinio https://epinio.github.io/helm-charts
After that run the command bellow to update the helm repositories
$ helm repo update

After doing the steps above you are ready to deploy epinio 
```
$ helm install epinio -n epinio --create-namespace epinio/epinio --set global.domain=192-168-49-100.sslip.io
```
Now that you depoloyed epinio you will need the CLI to interact with it
```
$ curl -o epinio -L https://github.com/epinio/epinio/releases/download/v1.5.0/epinio-linux-x86_64
```
```
$ chmod +x epinio
```
Now to check if everithyng is fine just run the Command bellow 
$ epinio version
if your output comes out like this
> epinio version
Epinio Version: v1.5.0
Go Version: go1.18
you had a sucefull installation of the epinio cli

Now to access epinio just type commnad bellow 
```
epinio login -u admin 'https://epinio.192-168-49-100.sslip.io'

Trust the certificate by pressing ```'y'``` and ```'enter'```
```
The default password is _"password"_. So use: 
```
$ epinio settings show
```
to verify if everything has running very well
Last Step 
Now to deploy the aplication 

inside the app path use:
```
epinio push --name sample-app  --path ../epinio-app
```
