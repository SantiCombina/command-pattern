from light import Light
from television import Television
from command import LightOnCommand, LightOffCommand, TVOnCommand, TVOffCommand
from remote_control import RemoteControl

if __name__ == "__main__":
    # Receptor
    living_room_light = Light()
    living_room_television = Television()

    # Comandos concretos
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    tv_on = TVOnCommand(living_room_television)
    tv_off = TVOffCommand(living_room_television)

    # Invocador
    remote = RemoteControl()

    # Encender la luz
    remote.set_command(light_on)
    remote.press_button()

    # Apagar la luz
    remote.set_command(light_off)
    remote.press_button()

    # Deshacer la acción anterior (Encender la luz de nuevo)
    remote.press_undo()

    # Encender la tv
    remote.set_command(tv_on)
    remote.press_button()

    # Deshacer la acción anterior (Apagar la tv)
    remote.press_undo()
