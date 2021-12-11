from fman import show_alert, OK, show_prompt, PLATFORM
from subprocess import Popen
from .settings import Settings

settings = Settings("Veracrypt")

class VeracryptHelper:
    def mountContainerNormalMode(self, file: str):
        args = []
        self._mount(file, args)

    def mountContainerTcMode(self, file: str):
        args = ['-tc']
        self._mount(file, args)

    def dismountAll(self):
        veracrypt = self._get_veracrypt()
        if(veracrypt):
            Popen([veracrypt, '-t', '-d'])

    def _mount(self, file, args):
        veracrypt = self._get_veracrypt()
        if(veracrypt):
            password = self._request_password()
            if(password):
                Popen([veracrypt, '-t'] + args + ['--non-interactive', '--mount', file, '-p', password])

    def _request_password(self):
        password, ok = show_prompt('Please enter the password')
        if password and ok:
            return password

    def _get_veracrypt(self) -> str:
        veracrypt = settings.get_application_path("Veracrypt")
        if veracrypt:
            return self._add_platform_specific_path(veracrypt)
        self._handle_veracrypt_not_found()
        return

    def _add_platform_specific_path(self, path) -> str:
        if PLATFORM == 'Mac':
            return path + '/Contents/MacOS/VeraCrypt'
        return path

    def _handle_veracrypt_not_found(self):
      print('Veracrypt not found')
      show_alert(
            'Veracrypt was not found',
            OK, OK
        )
