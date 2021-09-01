# Function to turn on 'Nachtmodus' if all entities from 'group.pyscript_nm_entities'
# stayed off for at least 900 seconds, otherwise timeout and do nothing
@task_unique("entities_on_off_pyscript")
@state_trigger("group.pyscript_nm_entities")
def entitiesOnOff():
    if group.pyscript_nm_entities == 'off':
        trig_info = task.wait_until(
                        state_trigger=("group.pyscript_nm_entities == 'on'"),
                        timeout=900
                    )
        if trig_info["trigger_type"] == "timeout":
            # 900 seconds elapsed without the entities stayed on; turn on
            if input_boolean.nachtmodus != "on":
                input_boolean.turn_on(entity_id="input_boolean.nachtmodus")
        else:
            # the entities stayed on for 900 seconds; turn off
            if input_boolean.nachtmodus != "off":
                input_boolean.turn_off(entity_id="input_boolean.nachtmodus")

# Function to turn off 'Nachtmodus' if any entity turn back to on
@task_unique("nachtmodus_off")
@state_trigger("group.pyscript_nm_entities == 'on'")
def triggeredOff():
    if input_boolean.nachtmodus != "off":
        input_boolean.turn_off(entity_id="input_boolean.nachtmodus")

# Function to turn off 'Nachtmodus' at 07:00
@task_unique("nachtmodus_off_cron")
@time_trigger("cron(0 7 * * *)")
def nachtmodusOff():
    if input_boolean.nachtmodus != "off":
        input_boolean.turn_off(entity_id="input_boolean.nachtmodus")
    if input_boolean.wohnzimmer_motion_manuell != 'off':
        input_boolean.turn_off(entity_id="wohnzimmer_motion_manuell")
