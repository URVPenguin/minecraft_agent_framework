class DependencyContainer:
    """"
    Global Dependency Container
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DependencyContainer, cls).__new__(cls, *args, **kwargs)
            cls._instance._registrations = {}
        return cls._instance

    def register(self, cls, instance = None):
        """
        Registers a class into container.

        Parameters
        ----------
        cls : class
        instance : class
        """
        if instance:
            self._registrations[cls] = instance
        else:
            self._registrations[cls] = cls

    def resolve(self, cls):
        """
        Resolves a registered dependency.

        Parameters
        ----------
        cls : class
            Class to resolve.

        Returns
        -------
        resolved : class
            Instance of the resolved class.
        """
        if cls not in self._registrations:
            raise ValueError(f"Dependency not found: {cls}")
        resolved = self._registrations[cls]
        if callable(resolved):
            resolved = resolved()
            self._registrations[cls] = resolved
        return resolved