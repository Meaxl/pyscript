import random

DEVICE_ID = 'ea6eee7ca05757dff5a83c94e7ac69bd'
MASTER_ID = 'light.wled_d1_mini_master'
DEPENDENT_ID = 'switch.music'
TIME_INTERVAL = '15m'

DEFAULT_EFFECT = 'Palette'
DEFAULT_INTENSITY = int(127)
DEFAULT_BRIGHTNESS = int(255)

DOMAIN = ['light', 'wled']
NAME = ['turn_on', 'turn_off', 'effect']
#SEGMENTS = ['light.wled_d1_mini_segment_1', 'light.wled_d1_mini_segment_2', 'light.wled_d1_mini_segment_3']

DEBUG = False

class Wled:
    def __init__(self):
        self.current_state = str
        self.random_palette = int
        self.random_speed = int
    
    def ledsState(self, master_id=MASTER_ID):
        self.current_state = state.get(master_id)
        return self.current_state
    
    def dependentState(self, dependent_entity=DEPENDENT_ID):
        self.dependent_entity = dependent_entity
        self.dependent_state = state.get(self.dependent_entity)
        return self.dependent_state
    
    def randomPalette(self, start: int, stop: int):
        self.p_start = start
        self.p_stop = stop
        self.random_palette = random.randrange(self.p_start, self.p_stop)
        return self.random_palette
            
    def randomSpeed(self, start: int, stop: int):
        self.s_start = start
        self.s_stop = stop
        self.random_speed = random.randrange(self.s_start, self.s_stop)
        return self.random_speed

class Services:
    def __init__(self, device_id=DEVICE_ID, master_id=MASTER_ID):
        self.domain = str
        self.name = str

        self.device_id = device_id
        self.master_id = master_id
    
    def setEffect(self, palette, speed, domain=DOMAIN[1], name=NAME[2], effect=DEFAULT_EFFECT, intensity=DEFAULT_INTENSITY):
        self.palette = palette
        self.speed = speed
        self.domain = domain
        self.name = name
        self.effect = effect
        self.intensity = intensity
        service.call(domain=self.domain, name=self.name, device_id=self.device_id, effect=str(self.effect), palette=self.palette, intensity=self.intensity, speed=self.speed)

    def turnOn(self, domain=DOMAIN[0], name=NAME[0], brightness=DEFAULT_BRIGHTNESS):
        self.domain = domain
        self.name = name
        self.brightness = brightness
        service.call(domain=domain, name=name, device_id=self.device_id, brightness=self.brightness)
    
    def turnOff(self, domain=DOMAIN[0], name=NAME[1]):
        self.domain = domain
        self.name = name
        service.call(domain=self.domain, name=self.name, entity_id=self.master_id)

@time_trigger(f'period(00:00:00, {TIME_INTERVAL})') # Cycle palette after defined TIME_INTERVAL
@state_active(f'{MASTER_ID} == "on"')
@service('pyscript.changepalette')
def changePalette():
    task.unique('changePalette')
    x = Wled()
    s = Services()
    x.ledsState()
    x.dependentState()
    x.randomPalette(0, 55)
    x.randomSpeed(50, 255)
    s.setEffect(x.random_palette, x.random_speed)
    if DEBUG is True:
        log.info('Leds Music: changing effect with arguments: "{0}, {1}, {2}, {3}, {4}, {5}, {6}"'.format(s.domain, s.name, s.device_id, s.effect, s.palette, s.intensity, s.speed))

@state_trigger(f'{DEPENDENT_ID} == "on"') # Turn the LEDs on if the DEPENDENT_ID is turned on
def dependentTurnedOn():
    task.unique('dependentTurnedOn')
    x = Wled()
    s = Services()
    x.ledsState()
    x.dependentState()
    if x.current_state != 'on':
        x.randomPalette(0, 55)
        x.randomSpeed(50, 255)
        s.setEffect(x.random_palette, x.random_speed)
        task.sleep(1)
        s.turnOn()
        if DEBUG is True:
            log.info('Leds Music: turned on by dependent_entity with arguments: "{0}, {1}, {2}, {3}"'.format(s.domain, s.name, s.device_id, s.brightness))
    else:
        log.info('Leds Music: Unknown error happend! Maybe Leds already turned on?')

@state_trigger(f'{DEPENDENT_ID} == "off"') # Turn the LEDs off if the DEPENDENT_ID is turned off
def dependentTurnedOff():
    task.unique('dependentTurnedOff')
    x = Wled()
    s = Services()
    x.ledsState()
    x.dependentState()
    if x.current_state != 'off':
        s.turnOff()
        if DEBUG is True:
            log.info('Leds Music: turned off by dependent_entity with arguments: "{0}, {1}, {2}"'.format(s.domain, s.name, s.master_id))
    else:
        log.info('Leds Music: Unknown error harrend! Maybe Leds already turned off?')

# @state_active(f'{DEPENDENT_ID}')
# def main():
#     x = Wled()
#     x.ledsState()
#     x.dependentState()

#     x.randomPalette(0,55)
#     x.randomSpeed(50,255)

#     s = Services(x.random_palette, x.random_speed)
#     if DEBUG == True:
#         log.info(x.ledsState())
#         log.info(x.current_state)
#         log.info(x.dependent_state)
