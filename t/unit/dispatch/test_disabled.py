

from thorn.dispatch.disabled import Dispatcher


def test_send():
    Dispatcher().send(data={'foo': 'bar'})
