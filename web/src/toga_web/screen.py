from toga.screen import Screen as ScreenInterface


class Screen:
    _instances = {}

    def __new__(cls, native):
        if native in cls._instances:
            return cls._instances[native]
        else:
            instance = super().__new__(cls)
            instance.interface = ScreenInterface(_impl=instance)
            instance.native = native
            cls._instances[native] = instance
            return instance

    def get_name(self) -> str:
        return "Web Screen"

    def get_origin(self) -> tuple[int, int]:
        return (0, 0)

    def get_size(self) -> tuple[int, int]:
        return self.native.clientWidth, self.native.clientHeight

    def get_image_data(self):
        self.interface.factory.not_implemented("Screen.get_image_data()")
