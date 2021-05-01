
.PHONY: clean jekyll

jekyll:
	jupyter jekyllnb --site_dir _site --page-dir _posts --image-dir assets/images _notebooks/*.ipynb
	python bin/jekyllfy-names.py "_posts/*.md"
