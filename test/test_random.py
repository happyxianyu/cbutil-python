import logging
from cbutil.util.random import *

def test_random():
    logging.info(make_uuid4_b64url_str())
    logging.info(make_uuid4_b58_str())

