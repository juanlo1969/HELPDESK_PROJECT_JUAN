"""
=========================================================================
 DataDesk Enterprise Helpdesk
 ------------------------------------------------------------------------
 Módulo      : backup.py
 Autor       : Juan Lorenzo Martín
 Versión     : 2.0
 Descripción :
     Gestión profesional de copias de seguridad para DataDesk.

 Funcionalidades implementadas en esta primera entrega:

     ✔ Creación automática de la carpeta backups
     ✔ Copia de seguridad manual
     ✔ Generación de nombres mediante fecha y hora
     ✔ Registro de eventos (Logging)
     ✔ Type Hints
     ✔ Manejo de excepciones

 NOTA:
     En la siguiente entrega se incorporarán:

         • Compresión ZIP
         • SHA256
         • Restauración
         • Limpieza automática
         • Programación automática
=========================================================================
"""

from __future__ import annotations

import shutil
import logging
from pathlib import Path
from datetime import datetime


class BackupManager:
    """
    ===============================================================
    Clase encargada de administrar todas las copias de seguridad
    del proyecto DataDesk.

    Esta clase será utilizada desde:

        • main.py
        • views.py
        • models.py

    siguiendo el principio de Separación de Responsabilidades (SoC).

    Responsabilidades:

        ✔ Crear carpeta backups
        ✔ Crear copias de seguridad
        ✔ Gestionar nombres únicos
        ✔ Registrar eventos

    ===============================================================
    """

    def __init__(
        self,
        source_file: str = "tickets.json",
        backup_folder: str = "backups",
        log_file: str = "logs/application.log"
    ) -> None:
        """
        Constructor de la clase BackupManager.

        Parámetros
        ----------

        source_file:
            Archivo principal que será respaldado.

        backup_folder:
            Carpeta donde se almacenarán las copias.

        log_file:
            Archivo donde se escribirán los eventos.
        """

        self.source_file = Path(source_file)
        self.backup_folder = Path(backup_folder)
        self.log_file = Path(log_file)

        # Crear directorios necesarios
        self._create_directories()

        # Configurar el sistema de logging
        self._configure_logging()

    # --------------------------------------------------------------

    def _create_directories(self) -> None:
        """
        Crea automáticamente los directorios necesarios
        si todavía no existen.

        Directorios:

            backups/
            logs/
        """

        self.backup_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    # --------------------------------------------------------------

    def _configure_logging(self) -> None:
        """
        Configura el sistema de registro de eventos.

        Todos los backups quedarán registrados en:

            logs/application.log
        """

        logging.basicConfig(

            filename=self.log_file,

            level=logging.INFO,

            format=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(message)s"
            ),

            encoding="utf-8"
        )

    # --------------------------------------------------------------

    def create_backup(self) -> Path:
        """
        Genera una copia de seguridad del archivo principal.

        Returns
        -------

        Path
            Ruta completa del backup creado.

        Raises
        ------

        FileNotFoundError

            Si tickets.json no existe.
        """

        if not self.source_file.exists():

            raise FileNotFoundError(

                f"No existe el archivo: {self.source_file}"
            )

        timestamp = datetime.now().strftime(

            "%Y-%m-%d_%H-%M-%S"

        )

        backup_name = (

            f"backup_{timestamp}.json"

        )

        backup_path = self.backup_folder / backup_name

        shutil.copy2(

            self.source_file,

            backup_path

        )

        logging.info(

            "Backup creado correctamente -> %s",

            backup_path

        )

        return backup_path

    # --------------------------------------------------------------

    def list_backups(self) -> list[Path]:
        """
        Devuelve todas las copias existentes.

        Returns
        -------

        list[Path]
        """

        backups = sorted(

            self.backup_folder.glob("backup_*.json"),

            reverse=True

        )

        return backups

    # --------------------------------------------------------------

    def last_backup(self) -> Path | None:
        """
        Devuelve el backup más reciente.

        Returns
        -------

        Path | None
        """

        backups = self.list_backups()

        if backups:

            return backups[0]

        return None

    # --------------------------------------------------------------

    def backup_exists(self) -> bool:
        """
        Indica si existe al menos una copia.

        Returns
        -------

        bool
        """

        return len(self.list_backups()) > 0


# ==============================================================
# Programa de prueba
# ==============================================================

if __name__ == "__main__":

    manager = BackupManager()

    print()

    print("=" * 60)
    print(" DataDesk Enterprise Backup Manager")
    print("=" * 60)

    try:

        backup = manager.create_backup()

        print("\nBackup creado correctamente\n")

        print(backup)

    except Exception as error:

        print("\nERROR\n")

        print(error)

    print("\nBackups disponibles:\n")

    for file in manager.list_backups():

        print(file)

    print("\nFin del programa.")