"""
Приложение, для управления e-mail адресами.
Точка входа.
"""

import controller
import view
import model
app = controller.Application(view.CLIView(), model.Email)
app.start()






