
.DEFAULT: install
.PHONY: install uninstall clean realclean
pkg := zsh-syntax-highlighting
REPO := git://github.com/zsh-users/zsh-syntax-highlighting.git

install:
	source ../pkgs_utils.sh; clone_update $(REPO)

# uninstall:
#     cd $(pkg); sudo make uninstall

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr $(pkg)
