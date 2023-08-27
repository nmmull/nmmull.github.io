global_deps=.deps

build:
	pandoc index.org -o index.html --template=.deps/home-template.html --lua-filter=.deps/links-org-to-html.lua

home: build
	open index.html

run: build
	open $(file)
