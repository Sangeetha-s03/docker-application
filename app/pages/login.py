from nicegui import ui


@ui.page("/")
def login_page():
    with ui.column().classes("w-full min-h-screen items-center justify-center bg-gray-100 p-4"):

        with ui.card().classes("w-full max-w-sm p-6 gap-4"):
            ui.label("Login").classes("text-2xl font-bold")

            ui.input("Email or Username").props("outlined").classes("w-full")

            ui.input(
                "Password",
                password=True,
                password_toggle_button=True,
            ).props("outlined").classes("w-full")

            ui.button("Login", on_click=lambda: ui.notify("Login clicked")).classes("w-full")

            ui.link("Forgot Password?", "#")