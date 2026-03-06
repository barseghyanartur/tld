import sys
import types
import pytest

from tld.base import BaseTLDSourceParser
from tld.trie import Trie


@pytest.fixture
def custom_tld_source_parser():
    """
    Dynamically injects `some.module` into sys.modules with a
    CustomTLDSourceParser class, then cleans up after the test.
    """

    # 1. Create the parent package "some" and the child module "some.module"
    some_pkg = types.ModuleType("some")
    some_pkg.__path__ = []  # marks it as a package
    some_mod = types.ModuleType("some.module")

    # 2. Define CustomTLDSourceParser as a real Python class
    class CustomTLDSourceParser(BaseTLDSourceParser):
        """A custom TLD source parser injected via fixture.

        `get_tld_names` must yield lines in Mozilla Public Suffix List format:
            - plain entries like "uk", "co.uk"
            - wildcard entries like "*.uk"
            - exception entries like "!metro.tokyo.jp"
            - blank lines and // comments are ignored

        For "http://www.google.co.uk" to resolve as "co.uk", we need both
        "uk" and "co.uk" registered so the parser picks the most specific
        match.
        """

        uid: str = "test-custom-parser"
        # A no-op placeholder URL — never fetched during tests since
        # get_tld_names is fully overridden and returns inline data
        source_url: str = "https://example.com/test-tld-list.dat"
        # Points to /dev/null so no real file I/O can occur
        local_path: str = "/dev/null"
        include_private: bool = True

        @classmethod
        def get_tld_names(
            cls,
            fail_silently: bool = False,
            retry_count: int = 0,
        ):
            # Return an iterator of (tld_string, private_domain: bool) tuples
            # or whatever the tld library expects from a parser
            trie = Trie()
            trie.add("uk", private=False)
            trie.add("co.uk", private=False)

            return {cls.local_path: trie}

    # 3. Attach the class to the module and wire up the package
    some_mod.CustomTLDSourceParser = CustomTLDSourceParser
    some_pkg.module = some_mod

    # 4. Inject into sys.modules
    sys.modules["some"] = some_pkg
    sys.modules["some.module"] = some_mod

    yield CustomTLDSourceParser  # optionally yield the class for direct use

    # 5. Cleanup — remove both entries so other tests aren't affected
    sys.modules.pop("some.module", None)
    sys.modules.pop("some", None)
