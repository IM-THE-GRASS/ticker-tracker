import reflex as rx
from ticker_tracker.state import State

def button():
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
    
    
def goal_card(info):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.card(
                rx.text(
                    info[0],
                    as_="div",
                    size="6",
                    margin_bottom="4px",
                    weight="bold",
                    color_scheme="green"
                ),
                rx.center(
                    rx.image(
                        src=f"{info[1]['imageURL']}",
                        max_height="65%",
                    ),
                    width="100%",
                    height="100%"
                ),
                
                height="40vh",
                width = "100%"
            ),
        ),
        rx.dialog.content(
            rx.text(
                f"Would you like to set your goal to {info[0]} for {info[1]['tickets']} tickets?",
                as_="div",
                size="6",
                margin_bottom="4px",
                weight="bold",
                color_scheme="green",
            ),
            rx.hstack(
                rx.image(
                    src=f"{info[1]['imageURL']}",
                    max_height = "40vh",
                    max_width= "80%"
                ),
                rx.vstack(
                    rx.text(
                        f"{info[0]:}",
                        as_="div",
                        size="6",
                        margin_bottom="4px",
                        weight="bold",
                        color_scheme="green"
                    ),
                    rx.cond(
                        info[1].contains("description"),
                        rx.text(
                            f"{info[1]['description']}",
                            as_="div",
                            size="3",
                            margin_bottom="4px",
                            weight="bold",
                            color_scheme="green"
                        ),
                        rx.box(),
                    ),
                    rx.text(
                        f"{info[1]['tickets']:} tickets",
                        as_="div",
                        size="8",
                        margin_bottom="4px",
                        weight="bold",
                        color_scheme="green"
                    ),
                    # rx.box(
                    #     rx.text(
                    #         "AAA",
                    #         position="absolute",
                    #         bottom="0",
                    #         left="0"
                    #     ), 
                    # ),
                    
                    
                    rx.box(
                        height="100%"
                    ),
                    
                    height="100%"
                ),
                
                overflow="hidden",
                height="100%"
                
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
                        on_click=lambda: State.set_goal(info)
                    ),
                    
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            
        )
        
    )
def change_goal():
    return rx.dialog.root(
        rx.dialog.trigger(
            button()
        ),
        rx.dialog.content(
            rx.flex(
                rx.text(
                    "Edit Goal",
                    as_="div",
                    size="6",
                    margin_bottom="4px",
                    weight="bold",
                    color_scheme="green"
                ),
                rx.scroll_area(
                    rx.grid(
                        rx.foreach(
                            State.shop_data,
                            goal_card,
                        ),
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    height="60vh"
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






    