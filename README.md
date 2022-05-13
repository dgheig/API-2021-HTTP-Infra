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



### Step 3: Reverse proxy with apache (static configuration)



### Step 4: AJAX requests with JQuery



### Step 5: Dynamic reverse proxy configuration





## Additional steps to get extra points on top of the "base" grade

### Load balancing: multiple server nodes (0.5 pt)



### Load balancing: round-robin vs sticky sessions (0.5 pt)



### Dynamic cluster management (0.5 pt)



### Management UI (0.5 pt)

We will use [Portainer-ce](https://docs.portainer.io/v/ce-2.9/)