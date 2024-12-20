class InjectedDependency:
    """
    Marks the injected dependency.
    """
    def __init__(self, dependency_type):
        self.dependency_type = dependency_type