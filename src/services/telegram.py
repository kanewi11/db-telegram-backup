import requests


class TelegramService:
    """A class for sending files to Telegram"""

    def __init__(self, bot_token: str, chat_id: str) -> None:
        self._chat_id = chat_id
        self.__telegram_url = (
            f"https://api.telegram.org/bot{bot_token}/sendDocument"
        )

    def send_document(self, file_path: str) -> None:
        """Sends the file to Telegram"""
        with open(file_path, "rb") as file:
            response = requests.post(
                url=self.__telegram_url,
                data={"chat_id": self._chat_id},
                files={"document": (file.name, file)},
            )
        if response.status_code != 200:
            raise RuntimeError(f"Failed to send document: {response.text}")
