
.PHONY: dist
dist:
	python ./setup.py sdist upload
	python ./setup.py bdist_wheel upload

.PHONY: register
register:
	python ./setup.py register

.PHONY: clean
clean:
	rm -fr build dist pkgs.egg-info src/__pycache__ upkg.egg-info/
