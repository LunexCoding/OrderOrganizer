from pathlib import Path
import os

from app.settingsConfig import settingsConfig
from app.backend.database.pipeline import DatabasePipeline
from queries import SqlQueries
from tools.fileSystem import FileSystem
from consts import Constants


class _Initializer:
    def __init__(self):
        self._enterprises = []

    def initializeDatabase(self):
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(SqlQueries.applyingSettings)
        databaseCreationPipeline.addOperation(SqlQueries.createTableOrder)
        databaseCreationPipeline.addOperation(SqlQueries.createTableClients)
        databaseCreationPipeline.addOperation(SqlQueries.createTableMachines)
        databaseCreationPipeline.addOperation(SqlQueries.createTableWorkshops)
        databaseCreationPipeline.addOperation(SqlQueries.createTableStages)
        databaseCreationPipeline.run()

    def run(self):
        if not FileSystem.exists(Constants.DATA_DIRECTORY):
            FileSystem.makeDir(Constants.DATA_DIRECTORY)
        if not FileSystem.exists(Path(Constants.DATA_DIRECTORY) / settingsConfig.DatabaseSettings["database"]):
            os.chdir(Constants.DATA_DIRECTORY)
            self.initializeDatabase()


g_initializer = _Initializer()
