global_deps=.deps

build:
	pandoc index.org -o index.html --template=.deps/home-template.html --lua-filter=.deps/links-org-to-html.lua
	pandoc policies.org -o policies.html --template=$(global_deps)/home-template.html --lua-filter=$(global_deps)/links-org-to-html.lua


home: build
	open index.html

run: build
	open $(file)
