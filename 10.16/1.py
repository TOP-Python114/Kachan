"""
Приложение, для управления e-mail адресами.
Точка входа.
"""

import controller
import view
import model


app = controller.Application(view.CLIView(), model.Email)
app.start()


# ИТОГ: вы можете лучше, не понижайте планку — 8/12
