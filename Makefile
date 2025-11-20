build:
	docker build -t traefik_estefany .

run:
	docker run -p 5000:5000 traefik_estefany

push:
	docker push ghcr.io/traefik_estefany/app:1.0.0
