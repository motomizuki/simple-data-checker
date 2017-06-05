import os
from .constants import *
from .templates import MIT_LICENSE, GIT_IGNORE, README, INIT, INPUT, CHECKER, OUTPUT

category_map = {
    "input": "in",
    "checker": "checker",
    "output": "out",
}


class PluginGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate(category: str, type_: str):
        package_name = '{}-{}-{}'.format(prod_name, category, type_)
        module_name = '{}_{}_{}'.format(prod_name, category, type_)
        class_name = '{}{}{}'.format(prod_name.title(), category.title(), type_.title())
        print("Creating {}/".format(package_name))
        os.makedirs(package_name, exist_ok=True)

        print("  Creating {}/LICENSE.txt".format(package_name))
        with open(os.path.join(package_name, 'LICENSE.txt'), 'w') as f:
            f.write(MIT_LICENSE)

        print("  Creating {}/.gitignore".format(package_name))
        with open(os.path.join(package_name, '.gitignore'), 'w') as f:
            f.write(GIT_IGNORE)

        print("  Creating {}/README.md".format(package_name))
        with open(os.path.join(package_name, 'README.md'), 'w') as f:
            f.write(README.format(prod_name=prod_name, category=category, type_=type_, yaml_category=category_map[category]))

        print("  Creating {}/lib/{}/__init__.py".format(package_name, module_name))
        os.makedirs(os.path.join(package_name, 'lib', module_name), exist_ok=True)
        with open(os.path.join(package_name, 'lib', module_name, '__init__.py'), 'w') as f:
            f.write(INIT.format(module_name, class_name))

        print("  Creating {}/lib/{}/{}.py".format(package_name, module_name, module_name))
        with open(os.path.join(package_name, 'lib', module_name, "{}.py".format(module_name)), 'w') as f:
            if category == "input":
                f.write(INPUT.format(class_name))
            elif category == "checker":
                f.write(CHECKER.format(class_name))
            elif category == "output":
                f.write(OUTPUT.format(class_name))
