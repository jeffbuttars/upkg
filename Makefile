.DEFAULT: install
.PHONY: install uninstall clean realclean

install:
	@for pkg in $$(ls -1) ; do \
		if [[ -d "$$pkg" ]]; then \
			if [[ -f "$$pkg/Makefile" ]]; then \
				echo "Running install on $$pkg"; \
				cd $$pkg; \
				make install; \
				cd -; \
			fi \
		fi \
	done

uninstall:
	@for pkg in $$(ls -1) ; do \
		if [[ -d "$$pkg" ]]; then \
			if [[ -f "$$pkg/Makefile" ]]; then \
				echo "Running install on $$pkg"; \
				cd $$pkg; \
				make uninstall; \
				cd -; \
			fi \
		fi \
	done

clean:
	@for pkg in $$(ls -1) ; do \
		if [[ -d "$$pkg" ]]; then \
			if [[ -f "$$pkg/Makefile" ]]; then \
				echo "Running install on $$pkg"; \
				cd $$pkg; \
				make clean; \
				cd -; \
			fi \
		fi \
	done

realclean:
	@for pkg in $$(ls -1) ; do \
		if [[ -d "$$pkg" ]]; then \
			if [[ -f "$$pkg/Makefile" ]]; then \
				echo "Running install on $$pkg"; \
				cd $$pkg; \
				make realclean; \
				cd -; \
			fi \
		fi \
	done

check:
	@for pkg in $$(ls -1) ; do \
		if [[ -d "$$pkg" ]]; then \
			if [[ -f "$$pkg/Makefile" ]]; then \
				echo "Running check on $$pkg"; \
				cd $$pkg; \
				make check; \
				cd -; \
			fi \
		fi \
	done
