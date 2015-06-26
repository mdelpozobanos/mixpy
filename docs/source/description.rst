===============================
mixpy
===============================

The following is a description/instructions of a Python's package template
based mainly in the blogs of `Jeff Knupp`_.

The templates characteristics are:

+ Free software: MIT license
+ Has the structure::

      .<root_folder>
      | - <prj_name>
      |    | - __init__.py
      |    ... subpackages and source files
      | - docs
      |    | - source
      |    |    | ... lots or .rst files
      |    | - Makefile
      | - requirements
      |    | - common.txt
      |    | - python2.7.txt
      |    | - python3.4.txt
      | - test
      |    ... same structure as <prj_name>, but each file preceded by *test_*
      | - LICENSE
      | - README.rst
      | - setup.py
      | - TODO
      | - tox.ini
      | - .gitignore

+ Uses a single definition of the package's **version** within *__init__.py*.
+ Suggests Git_: For version control.
+ Suggests Git-Flow_: To manage git workflow.
+ Suggests virtualenv_: To create virtual environments.
+ Suggests virtualenvwrapper_: To manage *virtualenv*.
+ Uses PyTest_: For code testing.
+ Uses Coverage_: For tracking test coverage.
+ Uses Tox_: For testing different environments.
+ Uses Flake8_: To check the coding style.
+ Sphinx_: Ready for Sphinx documentation auto-generator.
+ Travis-CI_: Ready for Travis Continuous Integration testing.
+ Suggest ReadTheDocs_: To publish the generated documentation.


-----------
__version__
-----------

The package's version is used in multiple places within the package. Having a
single definition of it reduces the chances of bugs. In this template, the
package's version is always read from the *__version__* variable within the
*__init__.py* file.


---
GIT
---

After `initiallizing GIT`_ in your machine, you can start using it for your
project.

1. Check the *.gitignore* file and make sure you're happy with it. This are
   rules for files ignored by GIT.

2. Initialize GIT within the root directory

  .. code-block:: bash

    git flow init

3. Add files to git

  .. code-block:: bash

    git add .

5. Initial commit. The following will automatically commit to the *develop*
   branch

  .. code-block:: bash

    git commit -m 'Initial commit'

Now you're ready. Some useful GIT commands/notes:

- Commit changes

  .. code-block:: bash

    git add -A
    git commit -m "commit message"

- List branches

  .. code-block:: bash

    git branch

Some useful GIT-FLOW commands/notes (apart from this `git-flog cheatsheet`_):

- "Feature branches typically exist in developer repos only, not in origin"
- Features

  .. code-block:: bash

    git flow feature start <feat_name>
    git flow feature finish <feat_name>

- Releases

  .. code-block:: bash

    git flow release start <rel_name> <BASE>
    git flow release finish <rel_name>


------
GitHub
------

If you want to upload the project to GitHub_ (for more information you can check
`this GitHub HowTo`_):

1. Create a new repository in GitHub. This is done straight from your GitHub
   account. Usually, the name of the repository is the same as the name of the
   project.

2. Add the project to the repository

  .. code-block:: bash

    git remote add origin https://github.com/<user_name>/<repo_name>.git

  .. Note:: If you set up your SSH keys, you should set the URL as

    .. code-block:: bash

      git remote add origin git+ssh://git@github.com/<user_name>/<repo_name>

    This will avoid you from entering the username and password every time you
    push something to GitHub

3. Pushing files into the repository

  .. code-block:: bash

    git push origin <branch_name>
    
4. Tracking a remote branch (in *origin*) to a local branch with same name

  .. code-block:: bash

    git branch -u origin/<branch_name>
   
   
-------------------
Virtual Environment
-------------------

Virtual environments are really cool to try out packages without messing with
the system

1. Make a v.e.:

  .. code-block:: bash

    mkvirtualenv <name>

  To specify a different python version than the default, use:

  .. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3 <name>

2. To activate a virtual environment run:

  .. code-block:: bash

    workon <name>

2. To deactivate a virtual environment run:

  .. code-block:: bash

    deactivate


-------
Sphinex
-------

Sphinx is a great tool to generate documentation.

1. Initialize sphinx:

  .. code-block:: bash

    sphinx-quickstart

  .. note:: It is recommended to set the following options

    - Set the root path to *docs*

    - Turn *autodoc* on

2. In *./docs/source/conf.py* add:

  + The root project directory is set as:

    .. code-block:: python

      sys.path.insert(0, os.path.abspath('../..'))

  + To allow numpy- and google-like documentation, add:

    .. code-block:: python

      extensions.append('sphinx.ext.napoleon')

  + To automatically generate a summary:

    .. code-block:: python

      extensions.append('sphinx.ext.autosummary')

  + To automatically load the packages version from the top *__init__.py* file:

    .. code-block:: python

        import io
        import re

        def find_version(*file_paths):
            # Finds the *__version__* of a package by reading it from
              *__init__.py*

            def read(*filenames, **kwargs):
                # Reads files and return their content in a single string
                encoding = kwargs.get('encoding', 'utf-8')
                sep = kwargs.get('sep', '\\n')
                buf = []
                for filename in filenames:
                    with io.open(filename, encoding=encoding) as f:
                        buf.append(f.read())
                return sep.join(buf)

            version_file = read(*file_paths)
            version_match = re.search('^__version__ = [\'](.+)[\']',
                                      version_file, re.M)

            if version_match:
                return version_match.group(1)
            raise RuntimeError("Unable to find version string.")

        # Extract release and version
        release = find_version('../../prj_template/__init__.py')
        version = '.'.join(release.split('.')[:2])

        # Be clean
        del io, re, find_version


3. In *./doc/source/index.rst* add the code to build the documentation page.

   Better jet! Use sphinx-apidoc_:

   .. code-block:: bash

     sphinx-apidoc -f -M -o docs/source prj_template/

   Then, edit the *index.rst* to include the generated *modules.rst* file and
   perhaps the README.rst and HISTORY.rst files. In this case, we have also
   created a *main.rst* file which gives a detailed description of the package.
   It is also included into the *index.rst* file.

4. Compile the html page

  .. code-block:: bash

    make html

  .. note:: To clean the documentation project run :

    .. code-block:: bash

      make clean


The following can be added to the *conf.py* file to configure marks of ignored
documentation code:

  .. code-block:: bash

    # The following code configures marks used to ignore documentation code
    from sphinx.ext.autodoc import between

    def setup(app):
        # Register a sphinx.ext.autodoc.between listener to ignore everything
        # between lines that contain the word <MARK>
        app.connect('autodoc-process-docstring', between('^.*<MARK>.*$',
                    exclude=True))
        return app

The following can be added to solve some numpydoc issue dealing with class
members:

  .. code-block:: bash

    # The following line solves some numpydoc issue dealing with class members
    numpydoc_show_class_members = False


-----------
ReadTheDocs
-----------

I haven't been able to build the documentation in ReadTheDocs. I keep getting
the error

.. code-block:: bash
  Could not import extension sphinx.ext.napoleon (exception: No module named
  sphinx.ext.napoleon)

The only solutions I have found are:

1. Forcing the use of napoleon 0.2.11
2. Importing it as 'sphinxcontrib.napoleon',

I have tried any possible combination of those without success. I give up for
now.


------------
Cookiecutter
------------

Cookiecutter is an awesome tool to create a template for your projects.
`Daniel Greenfeld`_ blog entry on Cookiecutter is a nice reading.


------------
Requirements
------------

A word about requirements. This is actually a little bit more complicated than
it looks a priory. Variable *install_requires* within *setup.py* and the file
*requirements.txt* are actually not redundant. Both are meant to be used in
different circumstances. Some reads about this by `Donald Stufft` and
and `Miguel Grinberg`_ are quite revealing. What I have taken from these is
that basic requirements should be specified within *setup.py*, while more
strict requirements should be specified in the file *requirements.txt*.

Remember to use the v.e. to create the package requirements.

.. code-block:: bash

  pip freeze -l > requirements.txt


-----------------------
Documentation Structure
-----------------------

Documentation must have the following information

* Code Example:  Provide code examples and explanations of how to use the
  project.

* Installation: Detailed explanation on how to install the package.

* API Reference: Depending on the size of the project, if it is small and
  simple enough the reference docs can be added to the README. For medium size
  to larger projects it is important to at least provide a link to where the
  API reference docs live.

* Tests: Describe and show how to run the tests with code examples.

* Contributors: Let people know how they can dive into the project, include
  important links to things like issue trackers, irc, twitter accounts if
  applicable.

* License: One line information about the license (LICENSE file inside the
  project folder)


.. _coverage: https://pypi.python.org/pypi/coverage
.. _Daniel Greenfeld: http://www.pydanny.com/cookie-project-templates-made-easy.html
.. _Donald Stufft: https://caremad.io/2013/07/setup-vs-requirement/
.. _flake8: https://flake8.readthedocs.org/en/2.3.0/
.. _git: http://git-scm.com/
.. _git-flow: https://github.com/nvie/gitflow
.. _git-flog cheatsheet: http://danielkummer.github.io/git-flow-cheatsheet/
.. _GitHub: https://github.com/
.. _initiallizing GIT: http://digital-madness.in/blog/2013/github-for-beginners-debianubuntulinux/
.. _Jeff Knupp: http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
.. _Miguel Grinberg: http://blog.miguelgrinberg.com/post/the-package-dependency-blues
.. _pytest: http://pytest.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _this GitHub HowTo: https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu-14.04/
.. _tox: https://tox.readthedocs.org
.. _TravisCI: https://travis-ci.org/
.. _Sphinx: http://sphinx-doc.org/index.html
.. _sphinx-apidoc: http://sphinx-doc.org/man/sphinx-apidoc.html
.. _virtualenv: https://virtualenv.pypa.io
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.org