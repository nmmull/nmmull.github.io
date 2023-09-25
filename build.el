;; load publishing
(require 'ox-publish)

;; Add the project to the publishing list
(setq org-publish-project-alist
      (list
	(list "personal website"
	 :base-directory "~/Developer/Repositories/nmmull.github.io"
	 :base-extension "org"
	 :publishing-directory "~/Developer/Repositories/nmmull.github.io"
	 :publishing-function 'org-html-publish-to-html
	 :section-numbers nil
	 :with-planning nil
	 :with-priority nil
	 :with-toc nil
	 :with-tasks nil
	 :headline-levels 1
	 :html-head-include-default-style nil
	 :html-head "<link rel=\"stylesheet\" href=\"globalStyle.css\">"
	 :html-preamble nil
	 :html-postamble nil)))

;; publish the website
(org-publish-all)
