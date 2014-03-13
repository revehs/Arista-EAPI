
from jsonrpclib import Server

switch = Server ( "http://admin:Qwer1234@20.0.2.24" )


response = switch.runCmds( 1, [ "enable" ,
                                "show interfaces description" ] ,
                                "text")

print response
