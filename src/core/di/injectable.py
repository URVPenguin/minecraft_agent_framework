from core.di.injected_dependency import InjectedDependency
from core.di.container import DependencyContainer

class Injectable:
    """
    Base class for all classes that have injected dependencies .
    Looking for the attributes that contain the :class:`InjectedDependency` class, and replacing it with the resolved dependency.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, value in self.__class__.__dict__.items():
            if isinstance(value, InjectedDependency):
                resolved = DependencyContainer().resolve(value.dependency_type)
                setattr(self, name, resolved)