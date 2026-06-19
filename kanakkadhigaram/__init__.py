"""
Kanakkadhigaram

Python implementation of mathematical methods found in the
ancient Tamil work 'Kanakkadhigaram'.

Subpackages
-----------
alaviyal
andaviyal
enn_arithal
nilam
porul_alavai
vaniga_kanakku
vivasaya_kanakku
"""

from .alaviyal import *
from .andaviyal import *
from .enn_arithal import *
from .nilam import *
from .porul_alavai import *
from .vaniga_kanakku import *
from .vivasaya_kanakku import *

__version__ = "0.1.0"

__all__ = [
    name
    for name in globals()
    if not name.startswith("_")
]