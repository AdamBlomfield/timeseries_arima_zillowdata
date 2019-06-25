## base.py
## wrapper for all local imports

# set environment variables
from src.settings import *

# local imports
from src.clean_data import *
from src.model import *
from src.visualize import *

# import other custom functions not suitable for other categories.
from src.custom import *

#import make_data


def test_base():
    print('Base Module Imported')
    print('\nTesting local imports')
    test_clean_data()
    test_model()
    test_viz()
    test_custom()

    return None
