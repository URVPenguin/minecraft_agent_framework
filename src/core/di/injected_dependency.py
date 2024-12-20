from typing import Type

class InjectedDependency:
    """
    Marks the injected dependency.
    """
    def __init__(self, dependency_type: Type):
        self.dependency_type = dependency_type