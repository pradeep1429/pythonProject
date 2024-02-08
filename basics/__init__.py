print("Initializing package")

# Setting variable
package_var = "This is a package-level variable"

from .legb import *
from .functions import outer_function
__all__ = [func, outer_function()]