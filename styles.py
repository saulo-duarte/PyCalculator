# QSS - Stylesheet for the application

import qdarktheme
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: white;
        background: {PRIMARY_COLOR};
    }}

    PushButton[cssClass="specialButton"]:hover {{
        color: white;
        background: {DARKER_PRIMARY_COLOR};
    }}

    PushButton[cssClass="specialButton"]:pressed {{
        color: white;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "Primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
