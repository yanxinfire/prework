## Overview

This project consists of two components: a server component(api_server) and a client component(api_cli). 
The server component is a web server that stores user information in a MySQL database. The client component is
a user-friendly command-line client that allows CRUD (Create, Retrieve, Update, Delete) operations on users.
The functionalities of this project include:

- Creating a user based on a user definition YAML
- Listing users with optional specifications such as first name, last name, and number of items
- Retrieving a user with a user ID
- Updating an existing user with a user definition YAML
- Deleting a user with a user ID

These components work together to provide a comprehensive system for managing user information, with the server
component handling data storage and the client component providing a convenient interface for performing CRUD
operations.

## Prerequisites

### Python version

Python version should not be less than v3.8.0.

### Kubernetes versions

Kubernetes version should not be less than v1.21.0.

### Nginx and Mysql

If you do not have the nginx ingress controller installed on your Kubernetes
cluster, please update the `subnginx.enabled` value to `true` in the
deployment/helm/values.yaml file.

Similarly, if you do not have a MySQL database available in your environment,
please update the `submysql.enabled` value to `true` in
the deployment/helm/values.yaml file. 
The default root password for the MySQL database is set to `oracle`.

## Installation
1. Navigate to the root directory of the project and build the api_server
image using the following command:
```console
$ make all
```
2. Push the built image to your own container registry and 
update the image registry and repository values in the
`deployment/helm/values.yaml` file accordingly.

3. Install the api-server on your Kubernetes cluster using Helm
with the following command:
```console
$ helm install api-server deployment/helm/
```

4. Once the installation is complete, you should see the following deployments
and services deployed on your Kubernetes cluster.
```console
$ kubectl get deployments 
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
api-server                 1/1     1            1           164m
api-server-nginx-ingress   1/1     1            1           164m
mysql                      1/1     1            1           3d20h

$ kubectl get svc
NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
api-server                 ClusterIP      10.111.102.104   <none>        8080/TCP                     164m
api-server-nginx-ingress   LoadBalancer   10.104.34.36     <pending>     80:32169/TCP,443:32428/TCP   164m
kubernetes                 ClusterIP      10.96.0.1        <none>        443/TCP                      632d
mysql                      ClusterIP      10.105.24.145    <none>        3306/TCP                     3d20h
mysql-np                   NodePort       10.101.197.44    <none>        3306:30036/TCP               3d19h
```


## Demonstration
Prepare a test user definition yaml, in this demonstration, I create a user.yaml in $(project_root)/test_files/:
```console
$ cat test_files/user.yaml 
first_name: John
last_name: Wick
age: 20
```
Navigate to the api_cli directory:
```console
$ cd api_cli
```

In my case, the service of nginx ingress controller is 10.104.34.36 and the port is 80.

### api_cli Help
You could show the help for api_cli as following:
```console
$ python3 api_cli.py -h
usage: api-cli [-h] [-H HOST] [-p PORT] {user} ...

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  api server ip address
  -p PORT, --port PORT  api server port

user subcommands:
  {user}                sub operations
    user                user operations

$ python3 api_cli.py user -h
usage: api-cli user [-h] {create,list,get,update,delete} ...

positional arguments:
  {create,list,get,update,delete}
    create              create user
    list                list users
    get                 get user
    update              update user
    delete              delete user

optional arguments:
  -h, --help            show this help message and exit

$ python3 api_cli.py user create -h
usage: api-cli user create [-h] -f USER_FILE

optional arguments:
  -h, --help            show this help message and exit
  -f USER_FILE, --user_file USER_FILE
                        user definition yaml file
```

### Create user
Create a user by specify the user.yaml:
```console
$ python3 api_cli.py --host 10.104.34.36 --port 80 user create -f ../test_files/user.yaml 
create user successfully
```
### List users
List users we have created:
```console
$ python3 api_cli.py --host 10.104.34.36 --port 80 user list
|id  |first_name  |last_name   |age|
------------------------------------
|14  |John        |Wick        |20 |
```

### Get a user
Get a user by user ID:
```console
[root@node01 api_cli]# python3 api_cli.py --host 10.104.34.36 --port 80 user get -U 14
id          : 14
first_name  : John
last_name   : Wick
age         : 20
```

If user does not exist:
```console
$ python3 api_cli.py --host 10.104.34.36 --port 80 user get -U 144
the user can't be found
```

### Update a user
In this case, we change the user.yaml to:
```console
$ cat ../test_files/user.yaml 
first_name: John
last_name: Wick
age: 25
```
Then update a user by user ID and user definition file,:
```console
$ python3 api_cli.py --host 10.104.34.36 --port 80 user update -U 14 -f ../test_files/user.yaml 
update user successfully

$ python3 api_cli.py --host 10.104.34.36 --port 80 user list
|id  |first_name  |last_name   |age|
------------------------------------
|14  |John        |Wick        |25 |
```

### Delete a user
Delete a user by user ID. Because the logic doesn't get the user first, if the user doesn't exist, you still can
get a success response:
```console
$ python3 api_cli.py --host 10.104.34.36 --port 80 user delete -U 14
delete user successfully

$ python3 api_cli.py --host 10.104.34.36 --port 80 user list
|id  |first_name  |last_name   |age|
------------------------------------

```
