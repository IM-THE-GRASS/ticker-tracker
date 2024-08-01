from reflex_motion import motion
import reflex as rx

def settings():
    return motion(
        rx.center(
            rx.icon(
                "settings",
                size=92, 
            ),
            height="100%"
        ),
        bg="#30A46C",
        border_radius="50%",
        position="absolute",
        top="1vh",
        left="1vw",
        width="40",
        height="40",
        while_hover={"scale":1.05, },
        while_tap={"scale": 0.9, "rotate":999},
        transition={"type": "spring", "stiffness": 400, "damping": 17},
    ),