import reflex as rx

def change_goal():
    return rx.button(
        rx.hstack(
            rx.box(
                rx.icon(
                    "pencil",
                    size=30
                ),
                width="2vw",
                height="4vh",
            ),
            rx.text(
                "Change goal",
                color="#F5F5F5",
                font_size="4vh",
                font_family="Slackey",
            ),
            spacing="1vw",
        ),
        bg="#30A46C",
        border_radius="0.5vw",
        padding="2vh",
        position="absolute",
        top="60vh",
        left="40vw",
        width="20vw",
        height="40px",
    ),