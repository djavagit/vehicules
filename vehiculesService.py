from spyne import Application, rpc, ServiceBase, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

import os
port = int(os.environ.get('PORT', 17777))  # as per OP comments default is 17995


print('test')

vehicules = {"data": []}
vehicules["data"].append({"name": "Volkswagen ID.3 Pure Performance", "chargingTime": 450, "autonomy": 275})
vehicules["data"].append({"name": "Tesla Model 3", "chargingTime": 375, "autonomy": 380})
vehicules["data"].append({"name": "Tesla Model Y Performance", "chargingTime": 495, "autonomy": 425})
vehicules["data"].append({"name": "Dacia Spring Electric", "chargingTime": 300, "autonomy": 170})
vehicules["data"].append({"name": "Kia EV6 GT", "chargingTime": 510, "autonomy": 395})
vehicules["data"].append({"name": "BMW i4 eDrive40", "chargingTime": 525, "autonomy": 475})
vehicules["data"].append({"name": "Nissan Leaf", "chargingTime": 735, "autonomy": 225})

class VehiculeService(ServiceBase):
    @rpc(_returns=AnyDict)
    def all_vehicule(ctx):
        return vehicules


application = Application([VehiculeService], 'spyne.examples.hello.soap',
in_protocol=Soap11(validator='lxml'),
out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    print(f'Serve running on {port}')
    server = make_server('0.0.0.0', port, wsgi_application)
    server.serve_forever()
