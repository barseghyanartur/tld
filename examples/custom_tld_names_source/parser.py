import os

from tld.utils import BaseMozillaTLDSourceParser

__all__ = ("CustomMozillaTLDSourceParser",)


class CustomMozillaTLDSourceParser(BaseMozillaTLDSourceParser):
    uid = "custom_mozilla"
    local_path = os.path.join(
        "..",
        "..",
        "examples",
        "custom_tld_names_source",
        "res",
        "effective_tld_names_custom.dat.txt",
    )
