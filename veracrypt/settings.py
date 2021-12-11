from fman import show_alert, OK, CANCEL, show_file_open_dialog, PLATFORM, load_json, save_json, PLATFORM
from os.path import exists, splitdrive
import os
import sys
import json

_PLATFORM_APPLICATIONS_FILTER = {
    'Mac': 'Applications (*.app)',
    'Windows': 'Applications (*.exe)',
    'Linux': 'Applications (*)'
}

class Settings:
    def __init__(self, plugin):
        self.plugin = plugin
        self.settings_file = self.plugin + " Settings.json"

    def get_application_path(self, application):
        settings = self._load_settings()
        path = settings.get(application, None)
        if path:
            return path
        
        helper = ApplicationPathHelper(application)
        path = helper.ask_for_application()
        if not path:
            return None
        self._save_settings(application, path)
        return path

    def _load_settings(self):
        settings = load_json(self.settings_file, default={})
        return settings

    def _save_settings(self, application, path: str):
        save_json(self.settings_file, {application: path})

class ApplicationPathHelper:
    def __init__(self, application):
        self.application = application

    def ask_for_application(self):
        can_configure = self._can_configure_now()
        if not (can_configure):
            return None
        return self._pick_application()

    def _can_configure_now(self) -> bool:
        choice = show_alert(
            self.application + """ is currently not configured. Please choose location.""",
            OK | CANCEL, OK
        )
        return choice & OK

    def _pick_application(self) -> str:
        path = show_file_open_dialog(
            'Pick ' + self.application, self._get_applications_directory(),
            _PLATFORM_APPLICATIONS_FILTER[PLATFORM]
        )
        return path

    def _get_applications_directory(self) -> str:
        if PLATFORM == 'Mac':
            return '/Applications'
        elif PLATFORM == 'Windows':
            result = os.environ["ProgramW6432"]
            if not result or not exists(result):
                result = os.environ["ProgramFiles"]
            if not exists(result):
                result = splitdrive(sys.executable)[0] + '\\'
            return result
        elif PLATFORM == 'Linux':
            return '/usr/bin'
        raise RuntimeError("Not supported platform: '" + PLATFORM + \
            "'. Supported platforms are 'Mac', 'Windows' and 'Linux'")