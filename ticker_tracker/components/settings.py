from reflex_motion import motion
import reflex as rx
from ticker_tracker.state import State

def settings():
    return rx.dialog.root(
        rx.dialog.trigger(
            motion(
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
                width="110px",
                height="110px",
                while_hover={"scale":1.05, },
                while_tap={"scale": 0.9, "rotate":999},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
        ),
        rx.dialog.content(
            rx.flex(
                rx.text(
                    "Settings",
                    as_="div",
                    size="6",
                    margin_bottom="4px",
                    weight="bold",
                    color_scheme="green"
                ),
                rx.text(
                    "Shop URL:",
                    as_="div",
                    size="3",
                    margin_bottom="4px",
                    weight="bold",
                    color_scheme="green"
                ),
                rx.input(
                    placeholder="Enter your shop URL you get when you use the \"/shop\" command in the Hack Club Slack.",
                    color_scheme="green",
                    value=State.shop_url,
                    on_change= State.set_shop_url
                ),
                rx.text(
                    "Disclaimer: This info is not saved on any server and is stored on your local machine. Nobody else can see your ticket count.",
                    as_="div",
                    size="1",
                    margin_bottom="4px",
                    weight="bold",
                    color="#7B7B7B"
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        color_scheme="gray",
                        variant="soft",
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        "Save",
                        color_scheme="green",
                        on_click=State.update
                    ),
                    
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )

    