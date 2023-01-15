build:
	docker build . -t yo-app
debug:
	docker run -it --rm -p 3000:1769 --name yo-app --entrypoint /bin/bash yo-app
run:
	docker run -d --rm -p 3000:1769 --name yo-app yo-app
stop:
	docker stop yo-app