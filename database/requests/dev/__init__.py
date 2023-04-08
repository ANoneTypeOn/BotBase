# The dev class will inherit all methods from operator folder and overload methods if they exists in its own folder
import database.requests.maintenance as maintenance

from database.requests.operator import *

from .control import *
from .intelligence import *
