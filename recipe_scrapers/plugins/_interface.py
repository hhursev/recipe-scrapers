from abc import ABC, abstractmethod
from collections.abc import Iterable


class PluginInterface(ABC):
    """
    Interface that all "Plugins" (including the ones written by programmers
    using the package) should implement.

    Every plugin should have the following 2 methods implemented:

    - should_run
    - run
    """

    run_on_hosts: Iterable[str] = ("*",)
    run_on_methods: Iterable[str] = ("title",)

    @classmethod
    @abstractmethod
    def run(cls, decorated):
        pass

    @classmethod
    def should_run(cls, host, method):
        return cls._should_run_host_check(host) and cls._should_run_method_check(method)

    @classmethod
    def _should_run_host_check(cls, host):
        return "*" in cls.run_on_hosts or host in cls.run_on_hosts

    @classmethod
    def _should_run_method_check(cls, method):
        return method in cls.run_on_methods
