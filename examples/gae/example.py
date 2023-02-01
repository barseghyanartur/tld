from parser import GAEMozillaTLDSourceParser

from tld import get_tld

if __name__ == "__main__":
    print(
        get_tld(
            "http://www.google.co.uk", parser_class=GAEMozillaTLDSourceParser
        )
    )

    print(
        get_tld(
            "https://www.john.app.os.fedoraproject.org",
            parser_class=GAEMozillaTLDSourceParser,
        )
    )
