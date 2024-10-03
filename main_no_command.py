from light import Light
from television import Television

if __name__ == "__main__":
    # Instancias de los receptores (Luz y Televisión)
    living_room_light = Light()
    living_room_tv = Television()

    # Encender la luz directamente
    living_room_light.on()

    # Apagar la luz directamente
    living_room_light.off()

    # Encender la televisión directamente
    living_room_tv.on()

    # Apagar la televisión directamente
    living_room_tv.off()