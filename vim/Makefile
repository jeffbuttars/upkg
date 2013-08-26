.DEFAULT: install
.PHONY: install uninstall clean realclean

install:
	./install.sh

uninstall:
	rm -fr $(HOME)/.vim
	rm -fr $(HOME)/.vimrc

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr vim

check:
	cd vim; git st
