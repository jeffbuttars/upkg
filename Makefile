
.PHONY: dist
dist:
	python ./setup.py sdist upload
	python ./setup.py bdist_wheel upload

.PHONY: clean
clean:
	rm -fr build dist pkgs.egg-info
