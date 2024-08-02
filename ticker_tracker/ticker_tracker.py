import reflex as rx
from reflex_motion import motion
from ticker_tracker.state import State
from .components.change_goal_button import change_goal
from .components.settings import settings


@rx.page(on_load=State.update_ticket_text)
def index():
    return rx.box(
        
        
        # THIS ISA TEXT YEA
        
        motion(
            rx.text(
                State.ticket_text,
                font_size="8vh",
                font_family="Slackey, sans-serif",
                color="rgba(123.25, 255, 176.77, 0.94)",
                text_align="center",
            ),
            position="absolute",
            top="40vh",
            left="-16vw",
            width="132vw",
            height="23vh",
            while_hover={"scale":1.05, },
            while_tap={"scale": 1, "rotate":State.tickets_random_rot},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.text(
                f"You are {State.goal_percent}% of the way to your goal!",
                font_size="4.44vh",
                font_family="Slackey, sans-serif",
                color="#3DD68C",
                text_align="center",
            ),
            position="absolute",
            top="51vh",
            left="22vw",
            width="57vw",
            height="12vh",
            while_hover={"scale":1.05, },
            while_tap={"scale": 1, "rotate":State.goal_random_rot},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        
        
        
        
        # THESE ARE IMAGESZX
        
        
        
        
        motion(
            rx.image(
                src="https://cloud-837rvecwy-hack-club-bot.vercel.app/0111851_sp880-airpods-pro-2nd-gen.png",
                transform="rotate(4deg)",
            ),
            width="13vw",
            height="25vh",
            position="absolute",
            top="67vh",
            left="5vw",
            while_hover={"scale":1.1, "rotate":-4, },
            while_tap={"scale": 0.9},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.center(
                rx.image(
                    src="https://cloud-9zwbzfbtw-hack-club-bot.vercel.app/00image_from_ios-removebg-preview.png",
                    transform="rotate(-10deg)",
                    #width="19.5vw",
                    #height="37.5vh",
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