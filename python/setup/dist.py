"""Common for setup scripts."""

NAME = '__project_name__'

AUTHOR = "__author__"

AUTHOR_EMAIL = "__email__"

DESCRIPTION = "__one_sentence__"

PACKAGES = ['__my_package__']

KEYWORDS = "__keywords__"

INSTALL_REQUIRES = [
    '__package__name__>=__version__',
]

PACKAGE_DATA = {
    '__packege__': [
        '__path_1__',
        '__path_2__',
    ]
    # Example - translation files:
    # '__my_package__': [
    #     'lang/ru_RU/LC_MESSAGES/*.mo',
    # ],
}

DATA_FILES = [
    (
        '__destination__', [
            '__source__',
        ]
        # Example - default config file:
        # 'pdc_demo/data', [
        #     'pdc_demo/data/pdc_demo.json',
        # ]
    ),
]

CLASSIFIERS = [
    # https://pypi.org/classifiers/
    "__classifier__ :: __value__",
]
