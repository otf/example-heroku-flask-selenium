.PHONY: server
server:
	./result/bin/app.py

.PHONY: test-develop
test-develop:
	./result/bin/app.py &
	pytest --base-url http://localhost:5000

.PHONY: test-production
test-production:
	pytest --base-url https://example-heroku-flask-selenium.herokuapp.com

.PHONY: nix-build
nix-build:
	nix build

.PHONY: nix-server
nix-server: nix-build
	nix develop --command make server

.PHONY: nix-test-develop
nix-test-develop: nix-build
	nix develop --command make test-develop

.PHONY: nix-test-production
nix-test-production: nix-build
	nix develop --command make test-production
