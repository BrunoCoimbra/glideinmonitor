config = dict(
    GWMS_Log_Dir='C:\\Users\\Thomas\\Fermilab\\Indexing Sandbox\\NOSYNC_glidein_gfactory_instance',
    # Directory where GWMS Factory stores Logs
    Saved_Log_Dir="C:\\Users\\Thomas\\Fermilab\\Indexing Sandbox\\NOSYNC_SavedLogs",
    # Directory to save compressed versions of logs
    DB_Dir="C:\\Users\\Thomas\\Fermilab\\Indexing Sandbox\\NOSYNC_DBLOG",  # Directory for SQLite Database
    Log_Dir="C:\\Users\\Thomas\\Fermilab\\Indexing Sandbox\\NOSYNC_DBLOG",
    # Directory for storing logs from this script
    Warn_Level='INFO',  # Warn level for internal log system [INFO, WARNING, ERROR, NONE]
    Users={  # Users for Web Authentication
        "admin": "admin"
    },
    Port=8888,  # Port for the web server
    Host="127.0.0.1",  # Host the web server will listen on
)