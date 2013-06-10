.DEFAULT: install
.PHONY: install uninstall clean realclean
pkg=virtualcandy
REPO=git@jeffbuttars.com:users/jeff/virtualcandy

install:
	source  ~/pkgs/pkgs_utils.sh; clone_update $(REPO)

# uninstall:
#     cd $(pkg); sudo make uninstall

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr $(pkg)

check:
	cd $pkg; git st

