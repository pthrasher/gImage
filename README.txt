======
gimage
======

This is a simple python module mostly meant to be used on the command line. It's really simple, you pass it a search query, it queries google, and returns the first image it gets back. It's pretty damn addictive.
  
To use it on the command line, type: ``python -m gimage sarah silverman``
To use it in your project::

    #!/usr/bin/env python

    from gimage import get_image_url

    print get_image_url("sarah silverman")


`on github <http://github.com/pthrasher/gimage>`_.

