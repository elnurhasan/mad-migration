from madmigration.config.conf import Config
from madmigration.main import Controller

config = Config("test.yaml")

if __name__ == "__main__":
    a = MadMigration(config)
    a.prepare_tables()
    a.sourceDB.session.close()
    a.destinationDB.session.close()
    print(a.test_func())
