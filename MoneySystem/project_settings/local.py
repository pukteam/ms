from MoneySystem.project_settings import LOCAL, PROD

if LOCAL and not PROD:
    from ..settings_local import *
