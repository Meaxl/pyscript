import time
from common.timer import Timer
from .const import VACUUM, BATTERY, PRESENCE_SENSOR, COUNTER

DEBUG = True

class PresenceHome:
    def __init__(self):
        self._presence_sensor = "off" # state.get(PRESENCE_SENSOR)
        self._presence_state: bool = None

    @property
    def state(self):
        if self._presence_sensor:
            val = self._presence_sensor
            if val is not None:
                if val == "on":
                    self._presence_state = True
                    return self._presence_state
                elif val == "off":
                    self._presence_state = False
                    return self._presence_state
        return None

class TotalCleaningCount:
    def __init__(self):
        self._total_count = int(0) # state.get(COUNTER): int

    @property
    def totalCount(self):
        if self._total_count:
            return self._total_count
        return


class ValetudoVacuumEntity():
    def __init__(self):
        self._state = "docked" # state.get(VACUUM)
        self._battery_level = int(100) # state.get(BATTERY)

        self.STATE_CLEANING: bool = None
        self.STATE_MOVING: bool = None
        self.STATE_MANUALCONTROL: bool = None
        self.STATE_RETURNING: bool = None
        self.STATE_DOCKED: bool = None
        self.STATE_PAUSED: bool = None
        self.STATE_IDLE: bool = None
        self.STATE_ERROR: bool = None

    @property
    def state(self):
        if self._state:
            val = self._state
            if val ==  "cleaning":
                self.STATE_CLEANING = True
                return self.STATE_CLEANING
            elif val ==  "moving":
                self.STATE_MOVING = True
                return self._state, self.STATE_MOVING
            elif val ==  "manual_control":
                self.STATE_MANUALCONTROL = True
                return self._state, self.STATE_MANUALCONTROL
            elif val ==  "returning":
                self.STATE_RETURNING = True
                return self._state, self.STATE_RETURNING
            elif val == "docked":
                self.STATE_DOCKED = True
                return self._state, self.STATE_DOCKED
            elif val ==  "paused":
                self.STATE_PAUSED = True
                return self._state, self.STATE_PAUSED
            elif val == "idle":
                self.STATE_IDLE = True
                return self._state, self.STATE_IDLE
            elif val == "error":
                self.STATE_ERROR = True
                return self._state, self.STATE_ERROR
        return None

    @property
    def batteryLevel(self):
        if self._battery_level:
            val = self._battery_level
            if val is not None:
                return self._battery_level
        return None

def main():
    presence = PresenceHome()
    presence.state

    counter = TotalCleaningCount()

    vacuum = ValetudoVacuumEntity()
    vacuum.state

    if vacuum.STATE_IDLE == True or vacuum.STATE_DOCKED == True:
        if DEBUG: print("IDLE OR DOCKED")
        if vacuum.batteryLevel >= 80:
            if DEBUG: print("CURRENT BATTERY LEVEL: {0}".format(vacuum.batteryLevel))
            # START CLEANING IF NO PERSON IS CURRENTLY AT HOME
            presence.state
            if presence.state != True:
                counter.totalCount
                if counter._total_count < 1:
                    # service.call(domain="counter", name="increment", entity_id=COUNTER)
                    # service.call(domain="vacuum", name="start", entity_id=VACUUM)

                    # START A TIMER HERE
                    # STOP THE TIMER IF STATE OF VACUUM CHANGES FROM CLEANING TO DOCKED/IDLE
                    if DEBUG: print("START CLEANING, COUNTER == 0")
            else:
                if DEBUG: print("SOMEBODY IS AT HOME")
        else:
            if DEBUG: print("CURRENT BATTERY LEVEL: {0}! Needs to be >= 80 to start cleaning cycle".format(vacuum.batteryLevel))
            pass
    elif vacuum.STATE_MOVING: pass
    elif vacuum.STATE_MANUALCONTROL: pass
    elif vacuum.STATE_RETURNING: pass
    elif vacuum.STATE_PAUSED: pass
    elif vacuum.STATE_CLEANING: pass
    elif vacuum.STATE_ERROR:
        print("ERROR OCCURED: see Valetudo logs for more information")
    else:
        print("ERROR OCCURED: see Valetudo logs for more information")
