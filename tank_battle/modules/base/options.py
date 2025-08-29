RESOLUTIONS = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080)
]

class Options:
    def __init__(self):
        self._music_enabled = True
        self._fs_enabled = False
        self._fs_toggled = False
        self._language = "en"
        self._resolution_index = 2  # Default to 1280x720


    def music_enabled(self):
        return self._music_enabled


    def enable_music(self):
        self._music_enabled = True


    def disable_music(self):
        self._music_enabled = False


    def toggle_music(self):
        self._music_enabled = not self._music_enabled


    def fullscreen_enabled(self):
        return self._fs_enabled


    def fullscreen_toggled(self):
        fs_toggled = self._fs_toggled
        self._fs_toggled = False
        return fs_toggled


    def toggle_fullscreen(self):
        self._fs_toggled = True
        self._fs_enabled = not self._fs_enabled
    

    def set_language(self, lang):
        self._language = lang


    def get_language(self):
        return self._language


    def set_resolution(self, index):
        if index < 0 or index >= len(RESOLUTIONS):
            return
        self._resolution_index = index


    def get_resolution(self):
        return RESOLUTIONS[self._resolution_index]
    