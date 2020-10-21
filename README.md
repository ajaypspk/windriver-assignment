# Windriver Assignment

## Exectue Unit test & Code coverage
```bash
python .\app-unittest.py                                               
.....
----------------------------------------------------------------------
Ran 5 tests in 0.007s

$ coverage run  .\app-unittest.py                                        
.........
----------------------------------------------------------------------
Ran 9 tests in 0.015s
OK

$ coverage report                                                        Name                                                                                   Stmts   Miss  Cover
----------------------------------------------------------------------------------------------------------
app-unittest.py                                                                           56      0   100%
app.py                                                                                    42      6    86%
----------------------------------------------------------------------------------------------------------
TOTAL                                                                                     98      6    93%
```

## Build container image and start docker container
```bash
# build docker image
$ docker build -t ajaypspk/encrpt-decrypt-app .

# check app docker image
$ docker images

# start app from docker image
$ docker run --name test-app -p 5000:5000 ajaypspk/encrpt-decrypt-app
```

## Rest calls
### Health Check /api/health
```bash
$ curl --header "Content-Type: application/json" \
  --request GET \
  http://localhost:5000/api/health
```
output
```
{
  "input": "",
  "message": "",
  "output": "ok",
  "status": "success"
}
```  
  
### Encrypt /api/encrypt

```bash
$ curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"input": "My String to encrypt"}' \
  http://localhost:5000/api/encrypt
```
output:
```
{
  "input": "My String to encrypt",
  "message": "",
  "output": "TXkgU3RyaW5nIHRvIGVuY3J5cHQ=",
  "status": "success"
}
```
  
### Decrypt /api/decrypt
```bash  
$ curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"input": "TXkgU3RyaW5nIHRvIGVuY3J5cHQ="}' \
  http://localhost:5000/api/decrypt
```
output
```
{
  "input": "TXkgU3RyaW5nIHRvIGVuY3J5cHQ=",
  "message": "",
  "output": "My String to encrypt",
  "status": "success"
}
```

## Helm Deployment
```bash
$ cd helm-deployment/encrypt-decrypt-app/

$ helm lint .
==> Linting .
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed

# Create namespace on Openshift
$ oc new-project encrypt-decrypt-app Now using project "encrypt-decrypt-app" on server "https://2886795283-8443-kitek03.environments.katacoda.com:443".


$ helm upgrade --install encrypt-decrypt-app .
Release "encrypt-decrypt-app" does not exist. Installing it now.
NAME: encrypt-decrypt-app
LAST DEPLOYED: Wed Oct 21 15:20:52 2020
NAMESPACE: encrypt-decrypt-app
STATUS: deployed
REVISION: 1
TEST SUITE: None

$ oc get deployment                  
NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
encrpt-decrypt-app   1         1         1            0           20s

$ oc get svc                         
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP                   PORT(S)          AGE
encrpt-decrypt-app   LoadBalancer   172.30.217.44   172.29.67.185,172.29.67.185   5000:31882/TCP   50s

$ oc expose svc encrpt-decrypt-app   
route.route.openshift.io/encrpt-decrypt-app exposed

oc get route                       
NAME                 HOST/PORT                                                                                PATH   SERVICES             PORT   TERMINATION   WILDCARD
encrpt-decrypt-app   encrpt-decrypt-app-encrypt-decrypt-app.2886795283-80-kitek03.environments.katacoda.com          encrpt-decrypt-app   5000                 None
```
