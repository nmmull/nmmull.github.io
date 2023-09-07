global_deps=../.deps
local_deps=.deps

build:
	cp -r ~/CS132-Fall-2023/Assignments .
	cp -r ~/CS132-Fall-2023/Slides .
	pandoc schedule.org -o schedule.html --template=$(local_deps)/schedule-template.html --lua-filter=$(global_deps)/links-org-to-html.lua
	pandoc index.org -o index.html --template=$(local_deps)/course-template.html --lua-filter=$(global_deps)/links-org-to-html.lua
	pandoc info.org -o info.html --template=$(local_deps)/course-template.html --lua-filter=$(global_deps)/links-org-to-html.lua
	pandoc material.org -o material.html --template=$(local_deps)/course-template.html --lua-filter=$(global_deps)/links-org-to-html.lua
	pandoc policies.org -o policies.html --template=$(local_deps)/course-template.html --lua-filter=$(global_deps)/links-org-to-html.lua
home: build
	open index.html

run: build
	open $(file)
