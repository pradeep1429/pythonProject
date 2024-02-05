print("Initializing package")

# Setting variable
package_var = "This is a package-level variable"

from .legb import func
from .functions import *
__all__ = [func,Functions]