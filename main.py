#coding: utf8
import time
from server.server import *
from src.asyncore.asyncore import *
from utils.echo import *
from utils.files import *

if __name__ == '__main__':
	echo.log("Starting all emulator components...")
	start = int(round(time.time() * 1000))
	echo.log("Initializing: Server Manager.")
	server = tfm_server()
	echo.log("Listing the connection ports...")
	socket_config = eval(files.read("./files/socket.json"))
	for port in socket_config["ports"]:
		main_server = asyncore_server(server, socket_config["address"], port)
	echo.log("Server started on the following ports: {0}".format(server.listen))
	end = int(round(time.time() * 1000))
	echo.log("Emulator started in {0}ms.\n".format(end-start))