import keyboard
import os


file_path = os.path.abspath(__file__)
os.environ["keyboard_scan_path"] = file_path

def keyboard_states():
    """
    Module that scans for key strokes and returns the stroke name and type
        Event_type: up, down
    """
    key_stroke = keyboard.read_event()
    return key_stroke.name, key_stroke.event_type

