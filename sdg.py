import asyncio

from pydatacq import Siglent

import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal.windows import flattop

import pyvisa as pv
from pyvisa.constants import StatusCode


rm = pv.ResourceManager()


CHANNEL = ['C1','C2']

class SDG(Siglent):

    def __init__(self, ip, port=5025,pydatacq_delay=0.5,use_visa=True,query_delay=0.1):
        # For some reason the SDG1032X does not
        # like to get its SCPI commands too
        # quickly.
        super().__init__(ip,port,wait=query_delay)
        self._use_visa = use_visa


    #
    def MDWV(self, ch, type=None, parameter=None, value=None):
        if type is None:
            cmd = CHANNEL[ch] + ':MDWV ' + parameter + ',' + value
        else:
            cmd = CHANNEL[ch] + ':MDWV ' + type
        return self.send(cmd)


    #
    async def async_query_string(self, cmd, size=8000):
        s = await self.async_query(cmd)
        return s.decode('ascii')
    
    
    def send(self,cmd):
        if self._use_visa:
            device = f'TCPIP::{self.ip}::INSTR'
            sdg = rm.open_resource(device,query_delay=self._wait)
            sdg.timeout = 1000
            sdg.read_termination = None
            sdg.write(cmd)
            sdg.close()
        else:
            super().send(cmd)
        return
    