CLIMATES = state.names(domain="climate")
SENSOR = 'sensor.esp32_schlafzimmer_temperatur'

class EQ3BTSmartThermostat:
    def __init__(self, entity):
      self.entity_id = entity

    def updateCurrentTemperature(self, entity_id, sensorvalue):
        state.set(entity_id, current_temperature=float(sensorvalue))
        log.info('Setting Temp: {0}: {1}'.format(entity_id, sensorvalue))


class getTemperatureSensor:
    def __init__(self, entity):
        self.entity_id = entity
        self.sensorvalue = None
        self.f = None

    def validateValue(self):
        try:
            self.sensorvalue = state.get(SENSOR)
            self.f = float(self.sensorvalue)
            return self.f
        except Exception as e:
            return False
            log.error(e)

@service
def cycleAllDevices():
    for c in CLIMATES:
        #task.unique(c)
        g = getTemperatureSensor(c)
        s = EQ3BTSmartThermostat(c)
        if c == 'climate.eq3_badezimmer':
            sensorvalue = g.validateValue()
            if sensorvalue != False:
                finalvalue = sensorvalue - 0.5
                task.unique(c)
                s.updateCurrentTemperature(c, finalvalue)
            else:
                pass
        if c != 'climate.eq3_badezimmer':
            sensorvalue = g.validateValue()
            if sensorvalue != False:
                finalvalue = sensorvalue - 0.0
                task.unique(c)
                s.updateCurrentTemperature(c, finalvalue)
            else:
                pass
