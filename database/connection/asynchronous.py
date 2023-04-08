from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool

from basic import BaseConn, BasePool


class AsyncConn(BaseConn):
    def __init__(self, db_name: str, db_role: str, db_path: str):
        self.get_conninfo(db_name, db_role, db_path)
        self.conn = self.get_conn()

    def get_conn(self) -> AsyncConnection:
        """A function that will try to create connection to database"""
        db_conn = await AsyncConnection.connect(self.conn_info, min_size=1, max_size=3, autocommit=True)

        return db_conn

    async def shutdown(self):
        return self.conn.close()


class AsyncPool(BasePool):
    def __init__(self, db_name: str, db_role: str, db_path: str):
        self.get_conninfo(db_name, db_role, db_path)
        self.conn = self.get_pool()

    def get_pool(self):
        async def make_autocommit(conn: AsyncConnection):  # кастомизация подключений при их создании пулом
            await conn.set_autocommit(True)

        self.pool = AsyncConnectionPool(self.conn_info, min_size=1, max_size=3,
                                        configure=make_autocommit)

    async def shutdown(self):
        await self.pool.close()
