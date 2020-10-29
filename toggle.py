#!/usr/bin/python3

import pulsectl

a2dp_sink_name = "a2dp_sink_ldac"

def toggle():
    pulse = pulsectl.Pulse("profile-switcher")

    default_sink_name = pulse.server_info().default_sink_name
    profile = default_sink_name.split(".")[-1]
    card = next(filter(lambda x: "bluez" in x.name, pulse.card_list()))
    print(dir(card))

    new_profile = "headset_head_unit" if "a2dp_sink" in profile else a2dp_sink_name
    pulse.card_profile_set(card, new_profile)
    pulse.close()


if __name__ == "__main__":
    toggle()
