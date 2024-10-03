# Command Pattern Example

Este repositorio contiene un ejemplo simple de cómo funciona el **patrón de diseño Command**. El patrón Command es un patrón de comportamiento que encapsula solicitudes como objetos, permitiendo parametrizar métodos con diferentes solicitudes, poner en cola operaciones y soportar funcionalidades como "deshacer".

## Componentes del Patrón

Este ejemplo incluye los siguientes componentes básicos del patrón Command:

- **Command**: Define la interfaz para ejecutar operaciones.
- **ConcreteCommand**: Implementa la interfaz de `Command`, ejecutando una acción específica sobre un receptor.
- **Invoker**: Almacena y ejecuta los comandos.
- **Receiver**: Los objetos que ejecutan las acciones reales.
- **Client**: Crea los comandos y los asocia con un invocador.

### Archivos principales:

- `light.py`: Contiene la clase `Light` (Receptor).
- `television.py`: Contiene la clase `Television` (Receptor).
- `commands.py`: Contiene las clases de comando para encender y apagar la luz y la televisión.
- `remote_control.py`: Contiene la clase `RemoteControl` (Invoker).
- `main.py`: Ejecuta el ejemplo con el patrón Command.
- `main_no_command.py`: Muestra cómo sería el código sin usar el patrón Command.

### Ejecución del ejemplo

Este ejemplo muestra cómo encender y apagar dispositivos (una luz y una televisión), y además cómo implementar la funcionalidad de **deshacer**. La funcionalidad de "deshacer" es posible gracias al patrón Command, que permite almacenar comandos ejecutados y revertir sus acciones.

## Presentación

Este código fue realizado como parte de una presentación para la materia **Diseño de Sistemas** en la carrera de **Ingeniería en Sistemas**. Puedes ver la presentación completa aquí:  
[Link a la presentación en Canva](https://www.canva.com/design/DAGL_iwbTYo/sq9R1r8nJTZ612KdmHKoEA/edit?utm_content=DAGL_iwbTYo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
