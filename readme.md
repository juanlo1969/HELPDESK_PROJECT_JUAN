## readme de juan
# 🖥️ DataDesk Helpdesk System

![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)
![Architecture](https://img.shields.io/badge/Architecture-SoC%20%7C%20MVC-blueviolet.svg)
![Status](https://img.shields.io/badge/status-production--ready-success.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)
![Security](https://img.shields.io/badge/Security-Hardened-red.svg)

---

# 📋 Descripción del Proyecto

**DataDesk Helpdesk System** es una aplicación profesional de escritorio desarrollada en **Python** para la gestión integral de incidencias (Helpdesk).

El proyecto ha sido diseñado siguiendo principios de **Ingeniería del Software**, utilizando una arquitectura modular basada en el patrón **Separation of Concerns (SoC)**, permitiendo una clara separación entre la lógica de negocio, la persistencia de datos y la interfaz gráfica.

Su objetivo es proporcionar una plataforma intuitiva para registrar, consultar, modificar y gestionar incidencias técnicas mediante una interfaz gráfica moderna desarrollada con **Tkinter** y **ttk**.

La aplicación está orientada a pequeñas y medianas empresas, departamentos IT y centros de soporte técnico.

---

# 🎯 Objetivos del Proyecto

* Implementar un sistema completo de gestión de incidencias.
* Aplicar Programación Orientada a Objetos (POO).
* Implementar una arquitectura modular escalable.
* Garantizar la persistencia de datos.
* Facilitar futuras ampliaciones mediante bajo acoplamiento entre módulos.
* Desarrollar una interfaz gráfica profesional.
* Aplicar buenas prácticas de desarrollo y documentación.

---

# 🚀 Características Principales

| Funcionalidad                  | Descripción                                |
| ------------------------------ | ------------------------------------------ |
| ✅ Gestión completa de Tickets  | Alta, consulta, modificación y eliminación |
| 🔎 Búsqueda Inteligente        | Filtrado dinámico en tiempo real           |
| 📊 Dashboard de Métricas       | Estadísticas automáticas                   |
| 💾 Persistencia JSON           | Almacenamiento automático                  |
| 🎨 Interfaz Profesional        | Basada en Tkinter + ttk                    |
| 🔄 Actualización automática    | Refresco inmediato del TreeView            |
| 🛡 Validación de datos         | Evita registros incorrectos                |
| 🗑 Confirmación de eliminación | Protección ante borrados accidentales      |
| 📁 Arquitectura Modular        | Fácil mantenimiento                        |
| 📝 Logging                     | Registro de eventos y errores              |

---

# 🔐 Módulo de Seguridad

El proyecto incorpora un conjunto de medidas de seguridad orientadas a garantizar la integridad de la información y la estabilidad de la aplicación.

## Controles implementados

### ✔ Validación de entradas

Todos los campos introducidos por el usuario son validados antes de ser almacenados.

Se controla:

* Campos vacíos.
* Longitud máxima permitida.
* Caracteres no válidos.
* Formato de datos.

---

### ✔ Manejo seguro de excepciones

Toda operación crítica se encuentra protegida mediante bloques:

```python
try:
except:
finally:
```

Evitando el cierre inesperado de la aplicación.

---

### ✔ Integridad del fichero JSON

Antes de cargar la base de datos se verifica:

* Existencia del archivo.
* Formato JSON válido.
* Recuperación automática ante corrupción.

---

### ✔ Gestión de errores

El sistema registra automáticamente errores mediante el módulo:

```
logging
```

permitiendo auditorías posteriores.

---

### ✔ Confirmación de operaciones críticas

Las operaciones destructivas requieren confirmación del usuario.

Ejemplo:

* Eliminación de tickets.
* Cambio de estado.
* Cierre de la aplicación.

---

### ✔ Arquitectura desacoplada

La separación de responsabilidades reduce el riesgo de errores derivados del acoplamiento entre componentes.

```
Interfaz
      │
      ▼
Lógica de negocio
      │
      ▼
Persistencia JSON
```

---

### ✔ Preparado para futuras mejoras

La arquitectura permite incorporar fácilmente:

* Autenticación de usuarios.
* Control de acceso basado en roles (RBAC).
* Base de datos SQLite o PostgreSQL.
* Cifrado AES de la información.
* Integración con Active Directory.
* Registro de auditoría.
* Copias de seguridad automáticas.
* API REST.
💾 Módulo de Copias de Seguridad (Roadmap)

Como evolución del proyecto se plantea la incorporación de un módulo de copias de seguridad (Backup Manager) que permita proteger la información almacenada por la aplicación y facilitar su recuperación ante incidencias.

Objetivos
Garantizar la disponibilidad de los datos.
Evitar la pérdida de información por errores humanos o fallos del sistema.
Permitir la restauración rápida del histórico de tickets.
Automatizar el proceso de generación de copias de seguridad.
Funcionalidades previstas
📁 Copias de seguridad manuales mediante un botón en la interfaz.
⏱️ Copias de seguridad automáticas configurables (diarias, semanales o mensuales).
📦 Compresión de los archivos de respaldo en formato ZIP.
🗂️ Organización automática de las copias por fecha y hora.
🔄 Restauración de una copia de seguridad desde la aplicación.
🧹 Eliminación automática de copias antiguas según una política de retención configurable.
✔️ Verificación de la integridad de las copias antes de su restauración.
📝 Registro de todas las operaciones de backup y restauración mediante el sistema de logging.
Arquitectura propuesta
Usuario
    │
    ▼
Backup Manager
    │
    ├────────► Backup Manual
    │
    ├────────► Backup Programado
    │
    ├────────► Restauración
    │
    └────────► Verificación de Integridad
                    │
                    ▼
            Carpeta /backups
                    │
                    ├── backup_2026-07-30_10-00.zip
                    ├── backup_2026-07-31_10-00.zip
                    └── ...
Estructura prevista del proyecto
helpdesk_project/

├── backup.py
├── backup_manager.py
├── backups/
│      ├── backup_2026-07-30.zip
│      ├── backup_2026-08-01.zip
│      └── ...
Integración con la aplicación

El módulo se integrará de forma desacoplada siguiendo la arquitectura SoC del proyecto. Desde la interfaz gráfica se incorporará un nuevo menú "Copias de Seguridad" con las siguientes opciones:

Crear copia de seguridad.
Restaurar copia.
Ver historial de copias.
Configurar copias automáticas.
Abrir carpeta de respaldos.

La lógica de backup permanecerá independiente del resto de componentes, facilitando su mantenimiento y futuras ampliaciones.

Beneficios
Mayor resiliencia frente a fallos.
Protección frente a borrados accidentales.
Recuperación rápida de la información.
Mejora de la continuidad del servicio.
Preparación para entornos empresariales donde la protección del dato es un requisito esencial.

---

# 🏗 Arquitectura del Proyecto

```
helpdesk_project/

│
├── models.py
│      ├── Ticket
│      ├── TicketManager
│      └── Persistencia JSON
│
├── views.py
│      ├── Ventana Principal
│      ├── Formularios
│      ├── TreeView
│      ├── Buscador
│      └── Panel de Métricas
│
├── main.py
│
├── tickets.json
│
├── README.md
│
└── logs/
       application.log
```

---

# 🛠 Tecnologías Utilizadas

| Tecnología  | Uso                            |
| ----------- | ------------------------------ |
| Python 3.13 | Lenguaje principal             |
| Tkinter     | GUI                            |
| ttk         | Componentes gráficos           |
| JSON        | Persistencia                   |
| Logging     | Auditoría                      |
| Dataclasses | Modelo de datos                |
| Type Hints  | Tipado estático                |
| UUID        | Identificador único de tickets |

---

# 📊 Funcionalidades

## Gestión de Tickets

* Alta de incidencias
* Edición
* Eliminación
* Cambio de estado
* Priorización
* Categorización

---

## Dashboard

Muestra automáticamente:

* Total de tickets.
* Tickets pendientes.
* Tickets en proceso.
* Tickets resueltos.
* Tickets cerrados.

---

## Buscador Inteligente

Permite localizar incidencias mediante:

* ID
* Usuario
* Categoría
* Prioridad
* Estado
* Descripción

---

# 📸 Vista Previa

```
+-------------------------------------------------------------+
|                DataDesk Helpdesk System                     |
+-------------------------------------------------------------+
| Usuario: [______________]                                  |
| Categoría: [Hardware ▼]                                    |
| Prioridad:[Alta ▼]                                         |
|                                                             |
| Descripción:                                                |
| +----------------------------------------------+            |
| |                                              |            |
| +----------------------------------------------+            |
|                                                             |
| [ Crear Ticket ] [ Limpiar ]                               |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| ID | Usuario | Categoría | Prioridad | Estado | Fecha       |
+-------------------------------------------------------------+
| 1  | Juan    | Hardware  | Alta      | Nuevo  | 29/07/2026  |
| 2  | Ana     | Software  | Baja      | Cerrado| 28/07/2026  |
+-------------------------------------------------------------+
```

---

# ▶ Instalación

```bash
git clone https://github.com/juanlo1969/HELPDESK_PROJECT_JUAN.git

cd HELPDESK_PROJECT_JUAN

python main.py
```

---

# 📚 Buenas Prácticas Aplicadas

* Arquitectura SoC
* Programación Orientada a Objetos
* Principios SOLID
* Código documentado
* PEP-8
* Type Hints
* Docstrings
* Logging
* Manejo de excepciones
* Código reutilizable
* Bajo acoplamiento
* Alta cohesión

---

# 🔮 Mejoras Futuras

* Base de datos SQLite.
* PostgreSQL.
* Sistema de autenticación.
* Gestión de usuarios.
* Roles y permisos.
* Exportación PDF.
* Exportación Excel.
* Integración LDAP.
* Dashboard con gráficos.
* Notificaciones por correo.
* API REST.
* Cliente Web.
* Dark Mode.
* Copias de seguridad automáticas.
* Cifrado de información.
* Firma digital de tickets.

---

# 👨‍💻 Autor

**Juan Lorenzo Martín**

Ingeniería de Software • Python • Ciberseguridad • Automatización • Desarrollo de Aplicaciones de Escritorio

---

# 📄 Licencia

Este proyecto se distribuye bajo licencia **MIT**, permitiendo su uso, modificación y distribución conforme a los términos de dicha licencia.

