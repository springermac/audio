import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

monitor = Gst.DeviceMonitor()
monitor.add_filter('Audio/Source')
devices = monitor.get_devices()
for device in devices:
    print(device.get_name())
    print(device.get_display_name())
    caps = device.get_caps()
    print(caps)
    for cap in caps:
        print(cap)
        print(cap.get_value('rate'))
    device_type = device.g_type_instance.g_class.g_type.name
    print(device_type)
    if device_type == 'GstOsxAudioDevice':
        print(device.props.device_id)
    elif device_type == 'GstWasapiDevice':
        print(device.props.device)
    elif device_type == 'GstDirectSoundSrcDevice':
        print(device.props.device_guid)
