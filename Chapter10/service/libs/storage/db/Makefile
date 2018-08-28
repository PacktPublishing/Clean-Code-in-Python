IMAGE:=pgimg

getdb:
	docker build -t $(IMAGE) .

rundb:
	docker run --name testpg \
		-p 5432:5432 \
		-v $(PWD)/sql:/usr/share/sql:z \
		-e POSTGRES_USER=$(DBUSER) \
		-e POSTGRES_PASSWORD=$(DBPASSWORD)\
		-e POSTGRES_DB=$(DBNAME) \
		-d $(IMAGE)

db: getdb rundb

_runscript:
	docker run -it --rm --link testpg:pgcli \
		-v $(PWD)/sql:/usr/share/sql:z \
		$(IMAGE) psql \
		-h testpg \
		-U $(DBUSER) \
		-d $(DBNAME) \
		-a -f /usr/share/sql/$(SCRIPT)

schema:
	make _runscript SCRIPT="schema.sql"

data:
	make _runscript SCRIPT="data.sql"

.PHONY: db getdb rundb _runscript schema data
