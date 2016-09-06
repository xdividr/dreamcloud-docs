# DreamCloud-docs
Documentation for users of all DreamCloud products (DreamCompute,
DreamObjects, etc). Aimed at developers who wish to learn how to use
DreamCloud standard APIs to automate common tasks.

The documentation is organized by product and level of knowledge
required to understand the documentation, stored in the source/
directory in sphinx formatted files. The source/ dir contains subdirs,
one for each of DreamCloud products and subdirs to group articles
based on depth of knowledge required by readers:

 - dreamcompute
   - gettingstarted
   - tutorials
   - api-docs
 - dreamobjects
   - gettingstarted
   - tutorials
   - api-docs

 ```note```: some of the directories above are empty and the content
you see in the Knowledge Base comes from other sources, like upstream
OpenStack docs forked by DreamHost and published automatically.

Building the Documentation
--------------------------

run `tox` in the repo to build the documentation, the build
directories are in build/html/$category/$section/$article. For
example, the dreamcompute tutorials documentation will be built to
"build/html/dreamcompute/tutorials/"

How to contribute
-----------------

Fork the repository, modify or add articles, run tox for basic syntax
checks and verify the built html locally before committing. Once
you're satisfied with the local results, create a pull request.

Gotchas of contributing
-----------------------

If you change a title of an article, you must first change it in the Knowledge
Base, this is because the publishing script compares articles by title and it
will create a new article with the new title if you dont change the article
title in the Knowledge Base.

Publishing to DreamHost Knowledge Base
--------------------------------------

The built html files are automatically published via Jenkins job to
(DreamHost Knowledge Base)[https://help.dreamhost.com] once merged
to master.

Hacks we have to make things pretty
-----------------------------------

 - If you create a TOC with labels using :ref: to refer to them, insert the
   TOC in '.. container:: table_of_content' and the Headers associated with
   each item in the TOC will remain at the top of the screen as you scroll past
   them

Styleguide
----------

Check the styleguide.rst for style requirements

Automation
----------

Things the script does:
 - Publish articles in the "source" directory (excluding things in the
    "common" directory)
 - Adds labels to the article in Zendesk from the rst meta
 - Puts the article in the section specified in the "section_id" file in the
    same directory as the rst file

Things the script does not do:
 - Rename articles in zendesk when their titles change
 - Delete articles that have been deleted from this git repo
