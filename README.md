# Slim SDK for python microservice in Cumulocity IoT
## Overview
This SDK is a small Cumulocity wrapper around the [tornado python web framework](http://www.tornadoweb.org/en/stable/). It simplifies the development of small docker based microservies designed to be hosted on top of [Cumulocity IoT](http://cumulocity.com/).

## Build & Delpoy

### 1. Build docker

```
$ docker build . -t <microservice-name>
```

### 2. Package for Cumulocity

```
$ docker save <microservice-name>:latest > image.tar
$ zip <microservice-name>.zip image.tar cumulocity.json
```

### 3. Deploy on Cumulocity

  see [managing applications](https://cumulocity.com/guides/users-guide/administration/#managing-applications)

## Local Testing

Every microservice in Cumulocity has unique bootstrap credentials that in the cloud are automatically injected.
In order to run the docker locally you will need to inject those environment variables so it can connect to your Cumulocity tenant in the cloud.

### 1. Create the microservice application

  You can either just upload the zip once or you can create an empty application via [REST](https://cumulocity.com/guides/microservice-sdk/rest/#microservice-development).

### 2. Retrieve the application ID

  If you chose the way via REST the response on creation will contain the ID otherwise you can also see it in the URL while you are on the detail page of your application (e.g. /apps/administration/index.html#/applications/**1337**/properties)
  
### 3. Retrieve bootstrap credentials

  You can retrieve the bootstrap credentials with the following request:
  ```
  GET /application/applications/{{applicationId}}/bootstrapUser
  ```
  
  The response will look similar to this:
  ```
  {
    "name": "servicebootstrap_my-microservice",
    "password": "test1234",
    "tenant": "mytenant"
  }
  ```
  
### 4. Start docker locally

  In order to run the docker locally you will need to add the 3 values for the bootstrap credentials, the Cumulocity url to connect to and you need to expose the port 80 to a port on your host system.
  Examples:

  ```
  docker run -p 8080:80 -e C8Y_BOOTSTRAP_TENANT=mytenant -e C8Y_BOOTSTRAP_USER=servicebootstrap_my-microservice -e C8Y_BOOTSTRAP_PASSWORD=test1234 -e C8Y_BASEURL=https://mytenant.cumulocity.com <microservice-name>
  ```
  
