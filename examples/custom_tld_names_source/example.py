from parser import CustomMozillaTLDSourceParser

from tld import get_tld

if __name__ == "__main__":
    print(
        get_tld(
            "http://www.google.bazar",
            parser_class=CustomMozillaTLDSourceParser,
        )
    )

    print(
        get_tld(
            "https://www.john.app.os.fedoraproject.bit",
            parser_class=CustomMozillaTLDSourceParser,
        )
    )
