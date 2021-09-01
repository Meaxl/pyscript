SENSOR = 'sensor.esp32_schlafzimmer_pm2_5'
AC_ENTITY = 'switch.schlafzimmer_airpurifier'
THRESHOLD_ABOVE = int(35)
THRESHOLD_BELOW = int(10)
TIME_PERIOD = '1m' # example: number{s|m|h|d|w}

def getCurrentState():
    if switch.schlafzimmer_airpurifier == 'off':
        pyscript.ac_current_state = str(False)
        getPM25Value()
    elif switch.schlafzimmer_airpurifier == 'on':
        if pyscript.ac_current_state == str(False):
            pyscript.ac_current_state = str(True)
            getPM25Value()
        else:
            pyscript.ac_current_state = str(True)
            getPM25Value()
    else:
        pass

def getPM25Value():
    global SENSOR
    global AC_ENTITY

    if input_boolean.nachtmodus == 'off' and input_boolean.movement == 'on' and binary_sensor.schlafzimmer_fenster_rechts == 'off' and binary_sensor.schlafzimmer_fenster_links == 'off':
        if pyscript.ac_current_state == str(False):
            if int(state.get(SENSOR)) >= int(THRESHOLD_ABOVE):
                # turn on airpurifier
                turnOnOff(AC_ENTITY, int(state.get(SENSOR)))
            else:
                pass
        elif pyscript.ac_current_state == str(True):
            if int(state.get(SENSOR)) <= int(THRESHOLD_BELOW):
                # turn off airpurifier
                turnOnOff(AC_ENTITY, int(state.get(SENSOR)))
            else:
                pass
        else:
            pass
    else:
        pass

def turnOnOff(ac_entity, pm25):
    if pyscript.ac_current_state == str(False):
        log.debug(f'CURRENT_STATE = off; service.call("switch", "turn_on", entity_id={ac_entity}")')
        service.call('switch', 'turn_on', entity_id=(f'{ac_entity}'))
        # logbook.log(entity_id=(f'{ac_entity}'), name='AC500', message=(f'Pyscript: AC500 turned on. Current PM2.5: {pm25}'), domain='switch')
        pyscript.ac_current_state = str(True)
    elif pyscript.ac_current_state == str(True):
        log.debug(f'CURRENT_STATE = on; service.call("switch", "turn_off", entity_id={ac_entity}")')
        service.call('switch', 'turn_off', entity_id=(f'{ac_entity}'))
        # logbook.log(entity_id=(f'{ac_entity}'), name='AC500', message=(f'Pyscript: AC500 turned off. Current PM2.5: {pm25}'), domain='switch')
        pyscript.ac_current_state = str(False)

@time_trigger(f'period(00:00:00, {TIME_PERIOD})')
def run():
    state.persist('pyscript.ac_current_state')
    getCurrentState()
