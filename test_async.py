import my_package.module
import asynctest
import asynctest.mock


class AsyncTestCase(asynctest.TestCase):
    @asynctest.mock.patch("async_package.gen.generate", return_value="mock")
    def test_decorator(self, mock):
        self.assertEqual((yield from my_package.module.method_async()), "mock")

    def test_ctx_manager(self):
        with asynctest.mock.patch("async_package.gen.generate",
                                  return_value="mock"):
            self.assertEqual((yield from my_package.module.method_async()),
                             "mock")

if __name__ == "__main__":
    asynctest.main()
