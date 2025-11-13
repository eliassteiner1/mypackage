
# so these imports would shorten the imports of f1 and f2
# when also exposing core in the main __init__: mypackage.core.funx.f1 -> mypackage.core.f1
from .funx import f1
from .funx import f2

from .funx import greet