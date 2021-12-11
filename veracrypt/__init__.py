from fman import DirectoryPaneCommand, ApplicationCommand, show_quicksearch, QuicksearchItem
from fman.url import as_human_readable
from .veracrypthelper import VeracryptHelper

helper = VeracryptHelper()

class MountInVeracryptTrueCryptMode(DirectoryPaneCommand):
    def __call__(self):
        selectedFile = as_human_readable(self.get_chosen_files()[0])
        helper.mountContainerTcMode(selectedFile)

class MountInVeracrypt(DirectoryPaneCommand):
    def __call__(self):
        selectedFile = as_human_readable(self.get_chosen_files()[0])
        helper.mountContainer(selectedFile)

class UnmountVeracryptVolume(ApplicationCommand):
    def __call__(self):
        result = show_quicksearch(self._get_items)
        if result:
            query, value = result
            if value:
                helper.dismount(value)
    def _get_items(self, query):
        result = helper.getMounts()
        for item in result:
            try:
                index = item.lower().index(query)
            except ValueError as not_found:
                continue
            else:
                highlight = range(index, index + len(query))
                yield QuicksearchItem(item, highlight=highlight)

class UnmountAllVeracryptVolumes(ApplicationCommand):
    def __call__(self):
        helper.dismountAll()
