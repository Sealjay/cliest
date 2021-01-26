from setuptools import setup

setup(
    name="Cliest",
    version="0.1",
    py_modules=["cliest"],
    install_requires=["click", "tabulate", "PyInquirer", "python-dotenv"],
    entry_points="""
        [console_scripts]
        cx=cliest:main
    """,
)