import datetime
import os


FILE_NAME = "../logs/log_"

class Logger:
    """
    Log implementation, logs date, time and a message (including ERROR/INFO tag).
    """
    def __init__(self ):
        # https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        log_file_name  = FILE_NAME + today + ".log"
        self.filename  = os.path.join(current_dir_path, log_file_name)

    def log(self, message: str) -> None:
        """
        Logs message with corresponding tag. 
        """
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"{timestamp}- {message}\n"

        with open(self.filename, "a") as f:
            f.write(log_entry)


