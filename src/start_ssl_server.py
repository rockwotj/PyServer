from test_app.framework.server.server import PieServer
from test_app.main import app

PieServer(app,port=8443,ssl=True).run()
