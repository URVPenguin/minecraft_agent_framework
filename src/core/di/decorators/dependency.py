from typing import Type
from core.di.container import DependencyContainer

def dependency(cls: Type) -> Type:
    """
    Decorator to register classes can be injected as a dependency.

    Parameters
    ----------
    cls : Type
        Decorated class.

    Returns
    -------
    cls: Type
    """
    DependencyContainer().register(cls)
    return cls