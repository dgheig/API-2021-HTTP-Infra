# Labo HTTP Infra

[TOC]

## Directives summary

### Objectives

* Learn (web infra, apache2 and express.js)
* Implement (dynamic web app HTML, CSS, JS + Ajax Requests)
* Practice (docker)



### General instructions

* Instructions are given through videos at each step (if correctly done, ensure a grade of 4.5)

* The rest of the points come from your own research and creativity.

* We can use other technologies if we want (apache $\Leftrightarrow$ nginx, express.js $\Leftrightarrow$ django, ...)

  > Go ahead, we **LOVE** that



Nb: Provide a way to see the result of each step individually (?)

## Required Steps (max grade: 4.5)

### Step 1: Static HTTP server with apache httpd

#### Goals

* Create a github repository
* Create a apache2 docker image with custom content



[startbootstrap.com](https://startbootstrap.com/): some bootstrap templates.

The template we used: [Freelancer](https://startbootstrap.com/theme/freelancer) [(download)](https://github.com/startbootstrap/startbootstrap-freelancer/archive/gh-pages.zip)

```bash
# Build
## Using Docker
docker build -f apache2.Dockerfile -t res-http-apache2-static .
## Using Docker compose
docker-compose build

# Run
## Using Docker
docker run -p "8080:80" res-http-apache2-static
## Using Docker compose (Build + Run)
docker-compose up # add -d option to run as a daemon (i.e in the background)
```



### Step 2: Dynamic HTTP server with express.js

#### Goals

* Write a dynamic HTTP app (express.js)
* Query the server (postman)



We made 3 versions:

* ExpressJs
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [CrowCpp](https://github.com/CrowCpp/Crow)

Nb: The CrowCpp server build is leveraged using a docker image with all the required build dependencies (see `step2/cpp/build.sh` script)



### Step 3: Reverse proxy with apache (static configuration)

#### Goals



#### [Virtualhost](https://httpd.apache.org/docs/2.4/en/vhosts/examples.html)

> Your server has multiple hostnames that resolve to a single address, and you want to respond differently for `www.example.com` and `www.example.org`.

This is especially useful when you want to [reverse-proxy](https://httpd.apache.org/docs/2.4/en/vhosts/examples.html#proxy) multiple hosts according to their domain or the port used.

```apache
<VirtualHost *:*>
    ProxyPreserveHost On
    ProxyPass        "/" "http://192.168.111.2/"
    ProxyPassReverse "/" "http://192.168.111.2/"
    ServerName hostname.example.com
</VirtualHost>
```

see [Reverse Proxy Guide](https://httpd.apache.org/docs/2.4/en/howto/reverse_proxy.html)



### Step 4: AJAX requests with JQuery



### Step 5: Dynamic reverse proxy configuration





## Additional steps to get extra points on top of the "base" grade

### Load balancing: multiple server nodes (0.5 pt)



### Load balancing: round-robin vs sticky sessions (0.5 pt)



### Dynamic cluster management (0.5 pt)



### Management UI (0.5 pt)

We will use [Portainer-ce](https://docs.portainer.io/v/ce-2.9/)