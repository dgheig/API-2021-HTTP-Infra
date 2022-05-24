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



see [Reverse Proxy Guide](https://httpd.apache.org/docs/2.4/en/howto/reverse_proxy.html)



* We used `*.localhost` domains to avoid dealing with DNS and updating configuration files.
* This is NOT possible to prevent access to containers from host. The containers are using interfaces on the host machine. **BUT** the browsers have a same-origin-policy which prevent cross-origin-resource-sharing, i.e. fetch data from another source than the current page's one
* Docker networks have their own dns resolution, we do not need to use static ip adresses and can use hostnames instead. This allow us to have 2 or more proxypass for the same host using `aliases`  to have multiple domains for each host.
* The apache static configuration will have to be updated manually each time a network change is made (change of ip/hostname, adding/removing service/replicas, ...)



### Step 4: AJAX requests with JQuery

#### Goals

* Use Jquery to make an AJAX request



* Jquery is not part of bootstrap anymore. We had to import it from a CDN.

  ```html
  <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
  ```

  

### Step 5: Dynamic reverse proxy configuration

#### Goals

* Use traefik for dynamic reverse proxy.



## Additional steps to get extra points on top of the "base" grade

### Load balancing: multiple server nodes (0.5 pt)

Automatique avec la configuration correct de traefik

![round-robin](img/round-robin.png)



### Load balancing: round-robin vs sticky sessions (0.5 pt)

TODO: activer le sticky session

### Dynamic cluster management (0.5 pt)

```bash
docker-compose scale static=3
```

![dynamic_cluster_management](img/dynamic_cluster_management.png)

TODO: Expliquer

### Management UI (0.5 pt)

We will use [Portainer-ce](https://docs.portainer.io/v/ce-2.9/).

```yaml
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - portainer-data:/data
    ports:
      - 9000:9000
```

Nb: We do not need special routing from traefik.

* The UI is available at `localhost:9000`.

* We need to configure a local docker by using the socket (available inside the container through a mount)

  ![add_local_docker](img/add_local_docker.png)