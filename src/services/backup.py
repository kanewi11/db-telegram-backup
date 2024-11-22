import subprocess
from dataclasses import dataclass, asdict


@dataclass(frozen=True, eq=False)
class Command:
    """Commands for different databases"""
    postgres: str = (
        'docker exec -i {container_name} '
        '/bin/bash -c "PGPASSWORD={db_password} '
        'pg_dump --username {db_user} {db_name}" > {backup_filename}'
    )
    mariadb: str = (
        'docker exec -i {container_name} '
        '/bin/bash -c "MYSQL_PWD={db_password} '
        'mariadb-dump -u {db_user} {db_name}" > {backup_filename}'
    )
    mysql: str = (
        'docker exec -i {container_name} '
        '/bin/bash -c "MYSQL_PWD={db_password} '
        'mysqldump -u {db_user} {db_name}" > {backup_filename}'
    )

    def dict(self) -> dict[str, str]:
        return {k: str(v) for k, v in asdict(self).items()}


class BackupService:
    """Class for working with database backups"""
    _command = Command().dict()

    def __init__(
        self,
        container_name: str,
        db: str,
        db_name: str,
        db_user: str,
        db_password: str,
    ) -> None:
        self._container_name = container_name
        self._db = db
        self._db_name = db_name
        self._db_user = db_user
        self.__db_password = db_password
        self._backup_filename = f"{db}_{db_name}.sql"

    def create_backup(self) -> str:
        """Creates a backup copy of the database"""
        command = self._generate_command()
        result = subprocess.run(
            args=command,
            shell=True,
            text=True,
            capture_output=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Backup failed:\n{result.stderr}")
        return self._backup_filename

    def _generate_command(self) -> str:
        """Generates a command to create a backup"""
        command = self._command.get(self._db)
        if not command:
            raise ValueError(f"Unsupported database type - {self._db}")
        return command.format(
            container_name=self._container_name,
            db_password=self.__db_password,
            db_user=self._db_user,
            db_name=self._db_name,
            backup_filename=self._backup_filename,
        )
