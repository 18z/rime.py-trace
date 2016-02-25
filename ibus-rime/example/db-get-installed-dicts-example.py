from engine.storage import DB

DB.open("/home/deanboole/.ibus/zime/zime.db")

print DB.get_installed_dicts()
