import os
import sys
from pathlib import Path

from src.core.factories import (
    get_backup_service,
    get_cleanup_service,
    get_telegram_service
)


def main() -> None:
    backup_service = get_backup_service()
    telegram_service = get_telegram_service()
    cleanup_service = get_cleanup_service()
    current_dir = Path(__file__).parent
    os.chdir(current_dir)
    try:
        backup_name = backup_service.create_backup()
        backup_path = current_dir.joinpath(backup_name)
        telegram_service.send_document(str(backup_path))
        cleanup_service.remove_file(str(backup_path))
        sys.stdout.write("Backup and upload successful")
    except Exception as error:
        sys.stdout.write(f"Error during backup process:\n{error}")


if __name__ == "__main__":
    main()
