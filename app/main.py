from nicegui import ui

from app.pages import login  


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Docker Application", port=8080, reload=False)