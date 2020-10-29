#!/usr/bin/python3

import pulsectl

def toggle():
    pulse = pulsectl.Pulse("profile-switcher")

    default_sink_name = pulse.server_info().default_sink_name
    profile = default_sink_name.split(".")[-1]
    card = next(filter(lambda x: "bluez" in x.name, pulse.card_list()))
    print(dir(card))

    new_profile = "headset_head_unit" if profile == "a2dp_sink" else "a2dp_sink"
    pulse.card_profile_set(card, new_profile)
    pulse.close()


if __name__ == "__main__":
    toggle()
