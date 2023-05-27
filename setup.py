import cx_Freeze

executables = [cx_Freeze.Executable('jogo_dino.py')]

cx_Freeze.setup(
    name='Google Dino Game',
    options={'build.exe': {'packages': ['pygame'],
                           'include_files': ['imagens', 'sons']}},
    executables=executables
)
