import uuid
import base64

__all__ = [
    'to_uuid4_b64url_str',
    'make_uuid4_b64url_str'
]


def to_uuid4_b64url_str(uuid):
    return base64.urlsafe_b64encode(uuid.bytes).decode(encoding='utf8')

def make_uuid4_b64url_str():
    return to_uuid4_b64url_str(uuid.uuid4())




