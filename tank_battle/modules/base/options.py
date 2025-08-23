class Options:
    def __init__(self):
        self._music_enabled = True
        self._fs_enabled = False
        self._fs_toggled = False
        self._language = "en"

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
    
