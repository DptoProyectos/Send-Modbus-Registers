#!/usr/aut_env/bin/python3.8

from modbusWrite import mbusWrite



# # Ejemplo #1 -------------------------------------------------------------------------------
# dlgid = 'YCHTEST'
# register = '2098'
# dataType = 'interger'               # interger | float
# value = 102
# mbusWrite(dlgid, register, dataType, value)
# # NOTA: El objetivo del llamado de la funcion en este caso es que se haga un envio de registros modbus a cierto datalogger.

# Ejemplo #2 -------------------------------------------------------------------------------
dlgid = 'YCHTEST'
mbusWrite(dlgid)
# NOTA: El objetivo del llamado de la funcion en este caso es enviar al datalogger los registros que se encuentren en la cola en caso de que hayan. En caso contrario la funcion no realiza nada. En casa de que hayan registros pendiente de envio, no se sacan nuevos registros de la cola hasta que no se coloque en NUL el campo MODBUS o BROADCAST de redis
            
                    
