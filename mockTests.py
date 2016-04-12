from sure import *
from mock import MagicMock

class Proxy:
    def get(self, i):
        pass
        
class Device:
    def __init__(self, proxy):
        self.cache = {}
        self.proxy = proxy

    def get(self, i):
        if(not (i in self.cache)):
            resp = self.proxy.get(i)
            self.cache[i] = resp
            return resp

        return self.cache[i]

def test_deviceGetCache():
    proxy = Proxy()
    proxy.get = MagicMock()
    proxy.get.return_value = "foo"

    device = Device(proxy)
    resp1 = device.get(1)
    resp2 = device.get(1)

    resp1.should.eql("foo")
    resp1.should.eql(resp2)
    
    proxy.get.assert_called_once_with(1)
