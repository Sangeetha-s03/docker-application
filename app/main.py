from nicegui import ui


@ui.page("/")
def home():
    ui.label("NiceGUI is working!")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Docker Application", port=8080, reload=False)