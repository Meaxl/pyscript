class VacuumAttachments(object):
    def __init__(self, a_dustbin=None, a_watertank=None, a_mop=None):
        self.dustbin = True # Get current state - sensor not created actually - from MQTT sensor
        self.watertank = False # Get current state - sensor not created actually - from MQTT sensor
        self.mop = False # Get current state - sensor not created actually - from MQTT sensor

        @property
        def dustBinState(self):
            if self._dustbin:
                val = self._dustbin
                if val is not None:
                    return self._dustbin
            return None

        @property
        def waterTankState(self):
            if self._watertank:
                val = self._watertank
                if val is not None:
                    return self._watertank
            return None

        @property
        def mopState(self):
            if self._mop:
                val = self._mop
                if val is not None:
                    return self._mop
            return None

def fetchStates():
    states = VacuumAttachments()
    print(states.dustbin, states.watertank, states.mop)
