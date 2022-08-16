Esta funcion es la que se encarga del envio modbus de registros hacia los PLCs o dataloggers. El envio se hace por lotes segun tamano del buffer definido y luego se comienza a llenar una cola del tipo FIFO que se va vaciando segun se vayan enviando los registros que tiene acumulados.


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
            
      