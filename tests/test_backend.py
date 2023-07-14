import unittest
from unittest import TestCase
from unittest.mock import patch
from datetime import datetime
from services.backend import insert_memory_to_db, SQLITE


class TestBackend(TestCase):

    @patch('services.backend.get_module_logger')
    def test_insert_memory(self, patch_module_logger):
        """
        checking to see if the added data can be retrieved from database
        """
        total, free, used = insert_memory_to_db()
        result = SQLITE.fetch_query(query="SELECT created_at FROM ram WHERE total=(?) AND free=(?) and used=(?) "
                                          "ORDER BY created_at DESC limit 1", params=(total, free, used))
        created_at = datetime.strptime(result[0][0], '%Y-%m-%d %H:%M:%S')
        self.assertAlmostEqual(datetime.timestamp(datetime.utcnow()), datetime.timestamp(created_at), delta=20)


if __name__ == '__main__':
    unittest.main()
