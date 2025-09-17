# 📬 Sistema de Gestión de Correos en Python

Este proyecto implementa un sistema básico de mensajería por correo utilizando programación orientada a objetos. Incluye funcionalidades para enviar, recibir, listar y organizar mensajes en carpetas como "inbox", "enviados" y "papelera".

## 🧠 Descripción

El sistema simula el comportamiento de un servidor de correo y sus usuarios. Cada usuario puede enviar y recibir mensajes, los cuales se almacenan en carpetas específicas. El diseño está basado en principios de abstracción, encapsulamiento y herencia.

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Programación orientada a objetos (OOP)
- Módulo `abc` para clases abstractas

## 📁 Estructura del proyecto

- `GestionCorreo`: Interfaz abstracta que define los métodos esenciales para la gestión de correos.
- `ServidorCorreo`: Clase que representa el servidor, gestiona usuarios registrados.
- `Usuario`: Implementa la interfaz `GestionCorreo`, representa un usuario con su email y carpetas.
- `Mensaje`: Clase que modela un mensaje con emisor, destinatarios, asunto y contenido.
- `Carpeta`: Clase que gestiona los mensajes dentro de una carpeta específica.

