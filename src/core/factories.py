from src.core.config import SETTINGS
from src.services.backup import BackupService
from src.services.cleanup import CleanupService
from src.services.telegram import TelegramService


def get_backup_service() -> BackupService:
    return BackupService(
        container_name=SETTINGS.container_name,
        db=SETTINGS.db,
        db_name=SETTINGS.db_name,
        db_user=SETTINGS.db_user,
        db_password=SETTINGS.db_password,
    )


def get_telegram_service() -> TelegramService:
    return TelegramService(
        bot_token=SETTINGS.bot_token,
        chat_id=SETTINGS.chat_id,
    )


def get_cleanup_service() -> CleanupService:
    return CleanupService()
