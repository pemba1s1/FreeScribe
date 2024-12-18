import ctypes
import os
import sys

def get_file_path(*file_names: str) -> str:
    """
    Get the full path to a files. Use Temporary directory at runtime for bundled apps, otherwise use the current working directory.

    :param file_names: The names of the directories and the file.
    :type file_names: str
    :return: The full path to the file.
    :rtype: str
    """
    base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath('.')
    return os.path.join(base, *file_names)

def get_resource_path(*filename: str, shared: bool = False) -> str:
    """
    Get the path to the files. Use User data directory for bundled apps, otherwise use the current working directory.

    :param filename: The name of the file.
    :type filename: str
    :return: The full path to the file.
    :rtype: str
    """
    if not hasattr(sys, '_MEIPASS'):
        return os.path.abspath(os.path.join(*filename))
    
    base = _get_user_data_dir(shared)
    freescribe_dir = os.path.join(base, 'FreeScribe')
    
    # Check if the FreeScribe directory exists, if not, create it
    try:
        if not os.path.exists(freescribe_dir):
            os.makedirs(freescribe_dir)
    except OSError as e:
        raise RuntimeError(f"Failed to create FreeScribe directory: {e}")
    
    return os.path.join(freescribe_dir, *filename)

def _get_user_data_dir(shared: bool) -> str:
    """
    Get the user data directory for the current platform.

    :return: The path to the user data directory.
    :rtype: str
    """
    if sys.platform == "win32": # Windows
        buf = ctypes.create_unicode_buffer(1024)
        ctypes.windll.shell32.SHGetFolderPathW(None, 0x001a, None, 0, buf)
        return buf.value
    elif sys.platform == "darwin": # macOS
        return "/Users/Shared/" if shared else os.path.expanduser("~/Library/Application Support")
    else: # Linux
        path = os.environ.get("XDG_DATA_HOME", "")
        if not path.strip():
            path = os.path.expanduser("~/.local/share") 
        return self._append_app_name_and_version(path)

