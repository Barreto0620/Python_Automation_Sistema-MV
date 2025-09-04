# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['CentBrowser.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Adicione aqui arquivos extras se necessário
        # ('config.ini', '.'),
        # ('assets/', 'assets/'),
    ],
    hiddenimports=[
        # Adicione imports não detectados automaticamente
        'selenium',
        'selenium.webdriver',
        'selenium.webdriver.chrome',
        'selenium.webdriver.common',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclua módulos desnecessários para reduzir tamanho
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
    ],
    noarchive=False,
    optimize=2,  # Otimização máxima
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Sistema_MV_Automation',  # Nome profissional
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compressão UPX para reduzir tamanho
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # REMOVIDO O CONSOLE - Invisível ao usuário
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Remova esta linha se não tiver ícone
    # version='version.txt',  # Comentado - remova se não tiver arquivo de versão
)