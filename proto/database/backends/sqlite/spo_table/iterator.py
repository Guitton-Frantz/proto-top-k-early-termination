import json

from datetime import datetime
from typing import Optional, List, Dict, Tuple

from proto.database.backends.db_iterator import DBIterator


class SQliteIterator(DBIterator):
    """A SQliteIterator implements a DBIterator for a triple pattern evaluated using a SQlite database file"""

    def __init__(self, cursor, connection, start_query: str, start_params: List[str], table_name: str, pattern: Dict[str, str], fetch_size: int = 500):
        super(SQliteIterator, self).__init__(pattern)
        self._cursor = cursor
        self._connection = connection
        self._current_query = start_query
        self._table_name = table_name
        self._fetch_size = fetch_size
        self._cursor.execute(self._current_query, start_params)
        self._buffer = self._cursor.fetchmany(size=1)
        self._last_read = None

    def last_read(self) -> str:
        """Return the index ID of the last element read"""
        if self._last_read is None or self._last_read == '':
            return self._last_read
        else:
            return json.dumps({
                's': self._last_read[0],
                'p': self._last_read[1],
                'o': self._last_read[2]
            }, separators=(',', ':'))

    def next(self) -> Optional[Tuple[str, str, str, Optional[datetime], Optional[datetime]]]:
        """Return the next solution mapping or None if there are no more solutions"""
        if len(self._buffer) == 0:
            self._buffer = self._cursor.fetchmany(size=self._fetch_size)
        if len(self._buffer) == 0:
            self._last_read = ''  # scan complete
            return None
        else:
            self._last_read = self._buffer.pop(0)
            return (
                self._last_read[0], self._last_read[1], self._last_read[2], None, None
            )
