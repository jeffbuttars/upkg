.DEFAULT: install
.PHONY: install uninstall clean realclean
pkg=vimpager

install:
	./install.sh

uninstall:
	cd $(pkg); sudo make uninstall

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr $(pkg)

check:
	cd $pkg; git st
