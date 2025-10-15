# modules/base_platform.py
class BasePlatform:
    def __init__(self, storage, config):
        self.storage = storage
        self.config = config

    def login(self):
        raise NotImplementedError

    def search_and_apply(self, keywords, location, max_jobs=5):
        """
        البحث وتقديم الطلبات — يجب أن تعيده كل منصة.
        """
        raise NotImplementedError
