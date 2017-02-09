import os

__title__ = 'tld.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'project_dir',
    'PROJECT_DIR',
)


def project_dir(base):
    """Project dir."""
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


PROJECT_DIR = project_dir
