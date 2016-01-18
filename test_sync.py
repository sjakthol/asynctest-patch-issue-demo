import my_package.module
import unittest
import unittest.mock


class SyncTestCase(unittest.TestCase):
    @unittest.mock.patch("sync_package.gen.generate", return_value="mock")
    def test_decorator(self, mock):
        self.assertEqual(my_package.module.method_sync(), "mock")

    def test_ctx_manager(self):
        with unittest.mock.patch("sync_package.gen.generate",
                                 return_value="mock"):
            self.assertEqual(my_package.module.method_sync(), "mock")

if __name__ == "__main__":
    unittest.main()
