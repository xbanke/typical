import typic

from apispec import BasePlugin, APISpec  # type: ignore


class TypicPlugin(BasePlugin):
    """A plugin for ``apispec`` which hooks into the schema registry for ``typical``.


    Examples
    --------
    >>> import apispec
    >>> import typic
    >>> from typic.ext.apispec import TypicPlugin, register
    >>> spec = apispec.APISpec("Foo API", "0.0.0", "3.0.2", plugins=[TypicPlugin()])
    >>> register(spec)
    """

    def schema_helper(self, name, definition, instance=None, **kwargs):
        return typic.schemas(primitive=True)["definitions"].get(name)


def register(spec: APISpec):
    """Register all known ``typical`` schemas to the APISpec.

    Parameters
    ----------
    spec
        The instance of :py:class:`APISpec` to register the schemas to.
    """
    for name, schema in typic.schemas(primitive=True)["definitions"].items():
        spec.components.schema(name, schema)
