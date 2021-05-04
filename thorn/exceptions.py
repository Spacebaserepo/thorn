"""Thorn-related exceptions."""



class ThornError(Exception):
    """Base class for Thorn exceptions."""


class ImproperlyConfigured(ThornError):
    """Configuration invalid/missing."""


class SecurityError(ThornError):
    """Security related error."""


class BufferNotEmpty(Exception):
    """Trying to close buffer that is not empty."""
