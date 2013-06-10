.DEFAULT: install
.PHONY: install uninstall clean realclean
REPO := git@jeffbuttars.com:users/jeff/pcm
pkg := pcm

install:
	source  ~/pkgs/pkgs_utils.sh; clone_update $(REPO)
	mkdir -p $(HOME)/bin
	ln -nvsf $(HOME)/pkgs/pcm/pcm/pcm $(HOME)/bin/pcm

uninstall:
	rm $(HOME)/bin/pcm

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr $(pkg)

check:
	cd $pkg; git st
