#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TomoHack/src/notes.py

"""Template script that follows a decent coding style.

It aims to cover basic Python functionality needed for the project.
First line calls 'shebang' (https://en.wikipedia.org/wiki/Shebang_(Unix)).
It is useful for running scripts (both shell and for interpreted languages)
in a UNIX environement. It also tells us humans what language (and version) was used to write the script you dealing with. This one is for Python 3.
Next we write 'docstring' explaining what this peice of code is about.
After that we importing modules (preferably in a certain order).
"""

import sys      # Python standard library (interpreter related functions)

__author__ = "Sergei Abramenkov"
__copyright__ = "Copyright 2022, NSU GeoHack"
__credits__ = ["Darina Ilyukhina", "Martina Terskaya", 
                "Kristina Potapova", "Vasiliy Potapov"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Sergei Abramenkov"
__email__ = "s.abramenkov@nsu.ru"
__status__ = "template"


"""We check if this file is running as a script and not an imported module.
If that is the case - we print number of supplied command line arguments.
And then simply iterating through them and printing each one.
"""

if __name__ == '__main__':
    print(f'Arguments count: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument {i:>6}: {arg}')

