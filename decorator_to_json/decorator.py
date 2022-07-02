import functools
import json

def to_json(foo):
    @functools.wraps(foo)
    def wrapped(*args, **kwargs):
        result = json.dumps(foo(*args, **kwargs))
        return result
    return wrapped
