from ignis import widgets
from ignis.app import IgnisApp
from .widgets import (
    QuickSettings,
    Brightness,
    VolumeSlider,
    User,
    Media,
    NotificationCenter,
    Battery
)
from .menu import opened_menu

app = IgnisApp.get_default()


class ControlCenter(widgets.RevealerWindow):
    def __init__(self):
        revealer = widgets.Revealer(
            transition_type="slide_left",
            child=widgets.Box(
                vertical=True,
                css_classes=["control-center"],
                child=[
                    widgets.Box(
                        vertical=True,
                        css_classes=["control-center-widget"],
                        child=[
                            QuickSettings(),
                            VolumeSlider("speaker"),
                            VolumeSlider("microphone"),
                            Brightness(),
                            Battery(),
                            User(),
                            Media(),
                        ],
                    ),
                    NotificationCenter(),
                ],
            ),
            transition_duration=300,
            reveal_child=True,
        )

        super().__init__(
            visible=False,
            popup=True,
            kb_mode="on_demand",
            layer="top",
            css_classes=["unset"],
            anchor=["top", "right", "bottom", "left"],
            namespace="ignis_CONTROL_CENTER",
            child=widgets.Box(
                child=[
                    widgets.Button(
                        vexpand=True,
                        hexpand=True,
                        css_classes=["unset"],
                        on_click=lambda x: app.close_window("ignis_CONTROL_CENTER"),
                    ),
                    revealer,
                ],
            ),
            setup=lambda self: self.connect(
                "notify::visible", lambda x, y: opened_menu.set_value("")
            ),
            revealer=revealer,
        )
