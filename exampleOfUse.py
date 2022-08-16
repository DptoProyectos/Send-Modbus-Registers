#!/usr/aut_env/bin/python3.8

from modbusWrite import mbusWrite



# Ejemplo #1 -------------------------------------------------------------------------------
dlgid = 'YCHTEST'
register = '2095'
dataType = 'interger'               # interger | float
value = 101

# llamo a la funcion para enviar el valor del registro
mbusWrite(dlgid, register, dataType, value)
            
                    
# si no hay datos llamo a la funcion por si le queda en cola algo para transmitir
# mbusWrite(self.dlgid, register=None, dataType=None, value=None, fdbk=rcv_mbus_tag_id, mbTag=rcv_mbus_tag_val)