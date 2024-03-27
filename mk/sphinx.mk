LOCALDIR = docs/
REMOTEDIR = ../www.co-pylit.org/www/tech-blog/
SSH_PORT = 5224

.PHONY: docsprep
docsprep:
	mkdir -p docs/_images/tikz

.PHONY:	docs
docs:	changes	## run Sphinx to build html pages
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

.PHONY: spelling
spelling:	## run tests on ci
	cd rst && \
		sphinx-build -b spelling -d _build/doctrees . ../docs

.PHONY:	docs-clean
docs-clean:	## clean docs for complete rebuild
		rm -rf rst/_build/doctrees

.PHONY: pdf
pdf:	## build PDF docs
	pip install . && \
	cd rst && \
	sphinx-build -b latex -d _build/doctrees . _build/latex && \
	cd _build/latex && \
	pdflatex pylit.tex && \
	cp pylit.pdf ../../../docs

.PHONY: sync
sync:	## upload docs to co-pylit
	rsync -avz -e "ssh -p $(SSH_PORT)" $(LOCALDIR) www.co-pylit.org:$(REMOTEDIR)


