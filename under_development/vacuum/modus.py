from .const import FANSPEED_STATE_SENSOR, WATERGRADE_SENSOR

class VacuumFanSpeed(object):
    def __init__(self, v_fanSpeed=None):
        self.fanSpeed = v_fanSpeed

    @property
    def fanSpeed(self):
        return self._fanSpeed

    @fanSpeed.setter
    def fanSpeed(self, new_fanSpeed):
        if type(new_fanSpeed) == str:
            self._fanSpeed = new_fanSpeed
            #state.setattr(FANSPEED_STATE_SENSOR, self._fanSpeed)
            print("state.setattr({0}, {1})".format(FANSPEED_STATE_SENSOR, self._fanSpeed))
        else:
            raise Exception("Invalid value for fanSpeed. Needs to be str type. Valid values are: low, medium, high, max")

class VacuumWaterGrade(object):
    def __init__(self, v_waterGrade=None):
        self.waterGrade = v_waterGrade

    @property
    def waterGrade(self):
        return self._waterGrade

    @waterGrade.setter
    def waterGrade(self, new_waterGrade):
        if type(new_waterGrade) == str:
            self._waterGrade = new_waterGrade
            #select.select_option(entity_id=WATERGRADE_SENSOR, option=self._waterGrade)
            print("entity_id={0}, option={1}".format(WATERGRADE_SENSOR, self._waterGrade))
        else:
            raise Exception("Invalid value for waterGrade. Needs to be str type. Valid values are: low, medium, high")

def changeFanSpeed():
    fs = VacuumFanSpeed("low")
    print(fs.fanSpeed)
    fs = VacuumFanSpeed("medium")
    print(fs.fanSpeed)
    fs = VacuumFanSpeed("high")
    print(fs.fanSpeed)
    fs = VacuumFanSpeed("max")
    print(fs.fanSpeed)

def changeWaterGrade():
    wg = VacuumWaterGrade("low")
    print(wg.waterGrade)
    wg = VacuumWaterGrade("medium")
    print(wg.waterGrade)
    wg = VacuumWaterGrade("high")
    print(wg.waterGrade)
