from psycopg import Connection
from psycopg_pool import ConnectionPool

from basic import BaseConn, BasePool


class SyncConn(BaseConn):
    def __init__(self, db_name: str, db_role: str, db_path: str):
        self.get_conninfo(db_name, db_role, db_path)
        self.conn = self.get_conn()

    def get_conn(self) -> Connection:
        """A function that will try to create connection to database"""
        db_conn = Connection.connect(self.conn_info, min_size=1, max_size=3, autocommit=True)
        return db_conn

    def shutdown(self):
        return self.conn.close()


class SyncPool(BasePool):
    def __init__(self, db_name: str, db_role: str, db_path: str):
        self.get_conninfo(db_name, db_role, db_path)
        self.conn = self.get_pool()

    def get_pool(self):
        def make_autocommit(conn: Connection):  # кастомизация подключений при их создании пулом
            conn.autocommit = True

        self.pool = ConnectionPool(self.conn_info, min_size=1, max_size=3,
                                   configure=make_autocommit)

    def shutdown(self):
        self.pool.close()
