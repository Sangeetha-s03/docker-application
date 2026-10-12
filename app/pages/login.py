import asyncio

from nicegui import ui

from app.validators import validate_password, validate_username


@ui.page("/")
def login_page():
    with ui.column().classes("w-full min-h-screen items-center justify-center bg-gray-100 p-4"):

        with ui.card().classes("w-full max-w-sm p-6 gap-4"):
            ui.label("Login").classes("text-2xl font-bold")

            username = ui.input(
                "Email or Username",
                validation=validate_username,
            ).props("outlined").classes("w-full")

            password = ui.input(
                "Password",
                password=True,
                password_toggle_button=True,
                validation=validate_password,
            ).props("outlined").classes("w-full")

            async def handle_login():
                username_ok = username.validate()
                password_ok = password.validate()
                if not (username_ok and password_ok):
                    return

                login_button.props("loading disable")
                username.disable()
                password.disable()

                try:
                    await asyncio.sleep(2)  
                finally:
                    login_button.props(remove="loading disable")
                    username.enable()
                    password.enable()

                ui.notify("Validation passed")

            login_button = ui.button("Login", on_click=handle_login).classes("w-full")