from fman import DirectoryPaneCommand
from fman.url import as_human_readable
from .veracrypthelper import VeracryptHelper

helper = VeracryptHelper()

class MountInVeracryptTCMode(DirectoryPaneCommand):
    def __call__(self):
        selectedFile = as_human_readable(self.get_chosen_files()[0])
        helper.mountContainerTcMode(selectedFile)

class UnmountAllVeracryptVolumes(DirectoryPaneCommand):
    def __call__(self):
        helper.dismountAll()
