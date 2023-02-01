from typing import Dict, Optional

from data import RAW_TLD_NAMES_DATA

from tld.base import BaseTLDSourceParser
from tld.exceptions import TldIOError
from tld.trie import Trie
from tld.utils import tld_names, update_tld_names_container


class GAEMozillaTLDSourceParser(BaseTLDSourceParser):

    uid: str = "gae_mozilla"
    source_url: str = "https://publicsuffix.org/list/public_suffix_list.dat"
    local_path: str = "gae_mozilla"

    @classmethod
    def get_tld_names(
        cls, fail_silently: bool = False, retry_count: int = 0
    ) -> Optional[Dict[str, Trie]]:
        """Parse.

        :param fail_silently:
        :param retry_count:
        :return:
        """
        if retry_count > 1:
            if fail_silently:
                return None
            else:
                raise TldIOError

        _tld_names = tld_names

        # If already loaded, return
        if (
            cls.local_path in _tld_names
            and _tld_names[cls.local_path] is not None
        ):
            return _tld_names

        try:
            local_file = RAW_TLD_NAMES_DATA.split("\n")
            trie = Trie()
            trie_add = trie.add  # Performance opt
            # Make a list of it all, strip all garbage
            private_section = False

            for line in local_file:
                if "===BEGIN PRIVATE DOMAINS===" in line:
                    private_section = True

                # Puny code TLD names
                if "// xn--" in line:
                    line = line.split()[1]

                if not line or line[0] in ("/", "\n"):
                    continue

                trie_add(f"{line.strip()}", private=private_section)

            update_tld_names_container(cls.local_path, trie)
        except IOError:
            # Grab the file
            cls.update_tld_names(fail_silently=fail_silently)
            # Increment ``retry_count`` in order to avoid infinite loops
            retry_count += 1
            # Run again
            return cls.get_tld_names(
                fail_silently=fail_silently, retry_count=retry_count
            )
        except Exception as err:
            if fail_silently:
                return None
            else:
                raise err
        finally:
            try:
                local_file.close()
            except Exception:
                pass

        return _tld_names
