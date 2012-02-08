#!/usr/bin/env python

import os
import site

from django.core.management import execute_manager
#import imp

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

site.addsitedir(path('apps'))

try:
    import settings_local as settings
except ImportError:
    try:
        import settings
    except ImportError:
        import sys
        sys.stderr.write(
            "Error: Tried importing 'settings_local.py' and 'settings.py'"
            "but neither could be found (or they're throwing an ImportError)."
            "Please come back and try later.")
        raise

## try:
##     imp.find_module('settings') # Assumed to be in the same directory.
## except ImportError:
##     import sys
##     sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
##     sys.exit(1)

## import settings

if __name__ == "__main__":
    execute_manager(settings)
