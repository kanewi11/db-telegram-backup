import os


class CleanupService:
    """Class for working with files (deleting, etc.)"""
    @staticmethod
    def remove_file(file_path: str) -> None:
        """Deletes the file at the specified path"""
        try:
            os.remove(file_path)
        except OSError as e:
            raise RuntimeError(f"Error removing file {file_path}: {e}")
