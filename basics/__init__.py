print("Initializing package")

# Setting variable
package_var = "This is a package-level variable"

from .functions import outer_function
from .legb import *

__all__ = [outer_function()]