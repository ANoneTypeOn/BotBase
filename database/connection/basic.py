from abc import ABC

from psycopg import Connection, AsyncConnection
from psycopg_pool import ConnectionPool, AsyncConnectionPool

from psycopg.conninfo import make_conninfo


class BaseStruct:
    conn_info: str

    def get_conninfo(self, db_name: str, db_role: str, db_path: str, db_port: int = 5432):
        """This method makes basic connection info string that will be available in local variable"""
        conn_dict = {'port': str(db_port), 'host': db_path, 'user': db_role, 'dbname': db_name}
        self.conn_info = make_conninfo('', **conn_dict)

    def shutdown(self):
        """This method stops the database connection instance and terminates it properly"""
        raise NotImplementedError

    def __del__(self):
        self.shutdown()


class BaseConn(BaseStruct, ABC):
    conn: Connection | AsyncConnection

    def get_conn(self) -> Connection:
        """This method generates the connection instance and places it in local variable"""
        raise NotImplementedError


class BasePool(BaseStruct, ABC):
    pool: ConnectionPool | AsyncConnectionPool

    def get_pool(self) -> ConnectionPool:
        """This method generates the pool instance and places it in local variable"""
        raise NotImplementedError
