import pytest
from core.di.container import DependencyContainer
from core.di.injectable import Injectable
from core.di.injected_dependency import InjectedDependency
from core.di.decorators.dependency import dependency
from core.di.decorators.inject import inject

container = DependencyContainer()

class TestClass:
    pass

def test_register_class():
    container._registrations = {}
    container.register(TestClass)

    assert TestClass in container._registrations, "Should contain TestClass"

def test_resolve_class():
    container._registrations = {}
    container.register(TestClass)
    resolved = container.resolve(TestClass)

    assert isinstance(resolved, TestClass), "Should return an instance of TestClass"

def test_resolve_instance():
    container._registrations = {}
    instance = TestClass()
    container.register(TestClass, instance)
    resolved = container.resolve(TestClass)

    assert resolved is instance, "Should return an instance of registered instance"


def test_resolve_unregistered_dependency():
    container._registrations = {}
    with pytest.raises(ValueError, match="Dependency not found: <class 'tests.test_di.TestClass'>"):
        container.resolve(TestClass)

def test_resolve_nested_dependencies():
    container._registrations = {}
    class DependencyA:
        pass

    class DependencyB:
        def __init__(self, dep_a: DependencyA):
            self.dep_a = dep_a

    container.register(DependencyA)
    container.register(DependencyB, lambda: DependencyB(container.resolve(DependencyA)))

    resolved_b = container.resolve(DependencyB)

    assert isinstance(resolved_b, DependencyB), "Should return an instance of DependencyB"
    assert isinstance(resolved_b.dep_a, DependencyA), "DependencyB should contain a DependencyA"

def test_override_dependency():
    container._registrations = {}
    class TestClassOverride:
        pass

    container.register(TestClass)
    container.register(TestClass, TestClassOverride())

    resolved = container.resolve(TestClass)

    assert isinstance(resolved, TestClassOverride), "Should return overwrite instance"

def test_singleton_behavior():
    container._registrations = {}
    class Singleton:
        instance = None

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    instance = Singleton()
    container.register(Singleton, instance)

    resolved1 = container.resolve(Singleton)
    resolved2 = container.resolve(Singleton)

    assert resolved1 is resolved2, "Should return same instance (singleton)"


def test_injected_dependency():
    container._registrations = {}
    id = InjectedDependency(TestClass)
    assert id.dependency_type == TestClass, "Should be equals to TestClass"

def test_inject():
    container._registrations = {}
    @dependency
    class Dependency:
        pass

    class TestClass2:
        dep: Dependency = inject(Dependency)

    assert isinstance(TestClass2().dep, InjectedDependency), "Should be an instance of InjectedDependency"

def test_injectable():
    container._registrations = {}
    @dependency
    class Dependency:
        pass

    class TestClass2(Injectable):
        dep: Dependency = inject(Dependency)

    assert isinstance(TestClass2().dep, Dependency), "Should be an instance of InjectedDependency"