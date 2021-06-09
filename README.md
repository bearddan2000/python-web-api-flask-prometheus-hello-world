# python-web-api-flask-prometheus-hello-world

## Description
Another way to serve web content.
Uses prometheus to track visitors.

To see a graph of visitors:
- Nav to http://localhost:81
- Classic UI
  - Click Graph tab
    - Search: 'scrape_samples_scraped'
    - Duration 1m

For health check:
- Nav to http://localhost:81
- Targetes

## Tech stack
- python
  - flask
- prometheus

## Docker stack
- python:latest
- prom/prometheus:latest

## To run
`sudo ./install.sh -u`
- Available http://localhost
- Prometheus console http://localhost:81

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- https://dev.to/camptocamp-ops/implement-prometheus-metrics-in-a-flask-application-p18
