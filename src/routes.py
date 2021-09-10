import importlib
import inspect
import pkgutil

from flask_classy import FlaskView

from utils.paths import APPS_PATH


def create_routes(app):
    """
    Register all EndPoints eg.
    App.register(app)
    :param app: Flask app create in main file project
    """
    # Register applications' views into the Flask app
    for loader, path, is_pkg in pkgutil.walk_packages([APPS_PATH], 'apps.'):
        if not is_pkg and '.api' in path:
            for class_name, class_def in inspect.getmembers(importlib.import_module(path), inspect.isclass):
                if issubclass(class_def, FlaskView) and class_def is not FlaskView:
                    class_def.register(app)

            # Execute start code on apps
            for func_name, func_def in inspect.getmembers(importlib.import_module(path), inspect.isfunction):
                if func_name == 'start':
                    func_def()
