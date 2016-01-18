A project that demonstrates problem in `asynctest.mock.patch` decorator of the
python [asynctest](https://github.com/Martiusweb/asynctest) library.

## STR
* Create a python3 virtualenv and run `pip install -r requirements.txt`
* Run `python test_async.py` to see the patching failure
* Run `python test_sync.py` to see the corresponding behavior of `unittest`
package.

## The problem
You have an async method in a library (here `async_package.gen.generate()`)
your module calls (here `my_package.module.method_async()`). When testing your
module (test in `test_async.py`), you want to mock out the call to the external
library.

The results are following:
* when `patch()` is a decorator of the test case, the original method is called
instead of the mocked one (patching failed)
* when `patch()` is used as a context manager, the mocked method is called
(correct)

`test_sync.py` performs a similar test using sync methods and the standard
unittest package and there patching works both as a decorator and as a context
manager (when used on a sync method).
