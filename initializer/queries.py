from app.backend.database.tables import DatabaseTables


class SqlQueries:
    applyingSettings = """PRAGMA foreign_keys = ON"""
    createTableOrder = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ORDERS} (
            `ID` INTEGER PRIMARY KEY,
            `Client_ID` INTEGER,
            `Date` Date,
            `Machine_Info` TEXT
        );
    """
    createTableClients = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.CLIENTS} (
            `ID` INTEGER PRIMARY KEY,
            `Enterprise` VARCHAR(255),
            `Phone` VARCHAR(11)
        );
    """
    createTableMachines = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.MACHINES} (
            `ID` INTEGER PRIMARY KEY,
            `Order_ID` INTEGER,
            `Active_stage` VARCHAR(255),
            `Completed_stages` TEXT
        );
    """
    createTableStages = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.STAGES} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `Description` TEXT,
            `Workshop_ID` INTEGER,
            FOREIGN KEY (Workshop_ID) REFERENCES {DatabaseTables.WORKSHOPS}(ID) ON DELETE SET NULL
        );
    """
    createTableWorkshops = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.WORKSHOPS} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `Stages_ID` VARCHAR(255),
            `Description` INTEGER
        );
    """
