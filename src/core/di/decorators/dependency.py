from core.di.container import DependencyContainer

def dependency(cls):
    """
    Decorator to register classes can be injected as a dependency.

    Parameters
    ----------
    cls : class
        Decorated class.

    Returns
    -------
    cls: class
    """
    DependencyContainer().register(cls)
    return cls