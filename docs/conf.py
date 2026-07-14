project = "Erexiva Gids voor Mannelijke Vitaliteit"
author = "Erexiva"
copyright = "2026, Erexiva"

extensions = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "Erexiva Active Man Formula"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0f70aa",
        "color-brand-content": "#0f70aa",
    },
    "dark_css_variables": {
        "color-brand-primary": "#6ec6ff",
        "color-brand-content": "#6ec6ff",
    },
}
