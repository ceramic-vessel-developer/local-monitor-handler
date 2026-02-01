from axela_devtools.monitoring import MonitoringHandler


class MonitoringHandlerImpl(MonitoringHandler):
    def check_camera_status(self) -> str:
        return "The camera is online and functioning normally."

    def check_darkness_level(self) -> str:
        return "The ambient light level is moderate. No low-light conditions detected."

    def check_outdoor(self) -> str:
        return "There is no one outdoor"
