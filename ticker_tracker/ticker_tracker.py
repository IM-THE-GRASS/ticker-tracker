import reflex as rx
from reflex_motion import motion
from ticker_tracker.state import State
from .components.change_goal_button import change_goal
from .components.settings import settings


#@rx.page(on_load=State.on_load)
def index():
    return rx.box(
        
        
        # THIS ISA TEXT YEA
        
        motion(
            rx.center(
                rx.desktop_only(
                    rx.text(
                        State.ticket_text,
                        font_size="7.5vh",
                        font_family="Slackey, sans-serif",
                        color="rgba(123.25, 255, 176.77, 0.94)",
                        text_align="center",
                        z_index = "9999",
                        position="relative"
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.text(
                        State.ticket_text,
                        font_size="5vh",
                        font_family="Slackey, sans-serif",
                        color="rgba(123.25, 255, 176.77, 0.94)",
                        text_align="center",
                        padding_bottom="20vh",
                        z_index = "20"
                    ),
                ),
                width="100%"
            ),
            
            
            position="absolute",
            top="35vh",
            width="100%",
            height="23vh",
            while_hover={"scale":1.05, },
            while_tap={"scale": 1, "rotate":State.tickets_random_rot},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.center(
                rx.cond(
                    State.has_goal,
                    rx.box(
                        rx.mobile_and_tablet(
                            rx.text(
                                f"{State.goal_percent}% to the {State.goal_name}!",
                                font_size="4.44vh",
                                font_family="Slackey, sans-serif",
                                color="#3DD68C",
                                text_align="center",
                                text_wrap="nowrap"
                            ),
                        ),
                        rx.desktop_only(
                            
                            rx.text(
                                f"You are {State.goal_percent}% to the {State.goal_name}!",
                                
                                font_size="4.44vh",
                                font_family="Slackey, sans-serif",
                                color="#3DD68C",
                                text_align="center",
                            ),
                        ),
                    ),
                    rx.box()
                ),
                
                width="100%",
            ),
            
            
            position="absolute",
            top="51vh",
            width="100%",
            height="12vh",
            while_hover={"scale":1.05, },
            while_tap={"scale": 1, "rotate":State.goal_random_rot},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        
        
        
        
        # THESE ARE IMAGESZX
        
        
        
        rx.desktop_only(
            motion(
                rx.image(
                    #src="https://cloud-837rvecwy-hack-club-bot.vercel.app/0111851_sp880-airpods-pro-2nd-gen.png",
                    src=State.random_img_2,
                    transform="rotate(4deg)",
                ),
                width="19.5vw",
                height="37vh",
                position="absolute",
                top="67vh",
                left="5vw",
                while_hover={"scale":1.1, "rotate":-4, },
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            motion(
                rx.image(
                    src=State.goal_img,
                    transform="rotate(4deg)",
                ),
                width="19.5vw",
                height="37vh",
                position="absolute",
                top="67vh",
                left="42vw",
                while_hover={"scale":1.1, "rotate":-4, },
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            motion(
                rx.center(
                    rx.image(
                        src=State.random_img_1,
                        transform="rotate(-10deg)",
                        #width="19.5vw",
                        #height="37.5vh",
                        on_mount=State.on_load
                    ),
                    width="100%",
                    height="100%"
                ),
                
                width="19.5vw",
                height="37.5vh",
                position="absolute",
                top="0vh",
                left="72vw",
                while_hover={"scale":1.05, "rotate":10, },
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
        ),
        
        
        
        
        
        change_goal(),
        settings(),
        
        
        
        overflow="hidden",
        width="100vw",
        height="100vh",
        position="relative",
        
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Slackey&display=swap"
    ],
)
app.add_page(index)