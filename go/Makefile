.DEFAULT: install

.PHONY: install uninstall clean realclean
install:
	./install.sh

uninstall:
	rm -fr go

clean:
	@echo "no clean"

realclean:
	rm -frv pkg src

check:
	git st
