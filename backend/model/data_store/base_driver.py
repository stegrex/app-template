from abc import ABC, abstractmethod

class BaseDriver(ABC):

    # TODO: Use standard docstring.
    """
    Return dictionary of success/error information.
    {}
    """
    @abstractmethod
    def commit():
        pass

    # TODO: Use standard docstring.
    """
    Return dictionary of success/error information.
    {}
    """
    @abstractmethod
    def rollback():
        pass

    # TODO: Use standard docstring.
    """
    Return tuple of responses
    (
        BaseObject,
        {}
    )
    """
    @abstractmethod
    def upsert(self, object=None, createdTime=None, expirationTime=None):
        pass

    # TODO: Use standard docstring.
    """
    Return tuple of responses
    (
        [BaseObject],
        {}
    )
    """
    @abstractmethod
    def filter_multiple(self, object, filter):
        pass
