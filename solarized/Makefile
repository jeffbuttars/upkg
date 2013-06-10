.DEFAULT: install
.PHONY: install uninstall clean realclean

install: xresources
	./install.sh
	cp -f xresources ~/.Xresources
	xrdb -merge ~/.Xresources

uninstall:
	@rm -vf /home/jeff/.kde/share/apps/konsole/Solarized\ Dark.colorscheme
	@rm -vf /home/jeff/.kde/share/apps/konsole/Solarized\ Light.colorscheme
	@rm -vf /home/jeff/.kde4/share/apps/konsole/Solarized\ Dark.colorscheme
	@rm -vf /home/jeff/.kde4/share/apps/konsole/Solarized\ Light.colorscheme

# clean:
#     cd $(pkg); make clean

realclean:
	rm -fr kde-colors-solarized

check:
	@echo ignored
