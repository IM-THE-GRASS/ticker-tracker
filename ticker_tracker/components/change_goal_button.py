import reflex as rx

def change_goal():
    return rx.box(
        rx.desktop_only(
            rx.button(
                rx.hstack(
                    rx.center(
                        rx.icon(
                            "pencil",
                            size=30
                        ),
                        width="2vw",
                        height="100%",
                    ),
                    rx.center(
                        rx.text(
                            "Change goal",
                            color="#F5F5F5",
                            font_size="4vh",
                            font_family="Slackey",
                            text_wrap="nowrap",
                        ),
                        height="100%",
                    ),
                    spacing="1vw",
                    height="100%"
                ),
                bg="#30A46C",
                border_radius="0.5vw",
                padding="2vh",
                position="absolute",
                top="60vh",
                left="40vw",
                width="23vw",
                height="40px",
            ),
        ),
        rx.mobile_and_tablet(
            rx.center(
                rx.button(
                    rx.hstack(
                        rx.center(
                            rx.text(
                                "Change goal",
                                color="#F5F5F5",
                                font_size="4vh",
                                font_family="Slackey",
                                text_wrap="nowrap",
                            ),
                            height="100%",
                        ),
                        spacing="1vw",
                        height="100%"
                    ),
                    bg="#30A46C",
                    border_radius="0.5vw",
                    padding="2vh",
                    width="45vw",
                    height="40px",
                ),
                position="absolute",
                top="60vh",
                width="100%",
                height="40px"
            )
            
        )
    )