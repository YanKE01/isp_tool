from datetime import datetime


class Utils:
    @staticmethod
    def format_message(message: str) -> str:
        """
        Format message with timestamp
        :param message: The message to format
        :return: Formatted message with timestamp
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp}: {message}"
        return formatted_message
