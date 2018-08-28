LISTEN_HOST:="0.0.0.0"
LISTEN_PORT:=8080
DBHOST:="127.0.0.1"
DBPORT:=5432

clean:
	find . -type d -name __pycache__ | xargs rm -fr {}
	find . -type d -name "*.egg-info" | xargs rm -fr {}

container:
	docker build -t deliveryimg .

service:
	docker run \
		--network=host \
		-p 8080:8080 \
		-e DBUSER=$(DBUSER) \
		-e DBPASSWORD=$(DBPASSWORD) \
		-e DBNAME=$(DBNAME) \
		-e DBHOST=$(DBHOST) \
		-e DBPORT=$(DBPORT) \
		-e LISTEN_HOST=$(LISTEN_HOST) \
		-e LISTEN_PORT=$(LISTEN_PORT) \
		-d deliveryimg

.PHONY: clean container service
