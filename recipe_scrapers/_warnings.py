class StaticValueWarning(Warning):
    """Emitted when a field is annotated as returning a fixed/static value."""

    ...


class FieldNotProvidedByWebsiteWarning(StaticValueWarning):
    """Emitted when a requested field doesn't seem to be provided by the recipe website."""

    ...
