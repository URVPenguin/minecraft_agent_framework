from core.di.injected_dependency import InjectedDependency

def inject(dependency_type) -> InjectedDependency:
    """
    Decorator to register classes can be injected as a dependency.

    Parameters
    ----------
    dependency_type : class
        Dependency type needed to inject.

    Returns
    -------
    InjectedDependency
    """
    return InjectedDependency(dependency_type)