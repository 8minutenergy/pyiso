from pyiso.base import BaseClient


class AESOClient(BaseClient):

    def get_generation(self, latest=False, yesterday=False, start_at=False, end_at=False, **kwargs):
        pass

    def get_trade(self, latest=False, yesterday=False, start_at=False, end_at=False, **kwargs):
        pass

    def get_load(self, latest=False, yesterday=False, start_at=False, end_at=False, **kwargs):
        pass

    def get_lmp(self, latest=False, yesterday=False, start_at=False, end_at=False, **kwargs):
        pass
