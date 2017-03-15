import importlib.util

spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
Tokenizer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Tokenizer)

class MathHandler(object):
