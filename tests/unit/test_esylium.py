import pytest
from src import Esylium

class TestEsylium(object):

    @pytest.fixture
    def instance(self):
        return Esylium()

    def test_constract(self, instance):
       assert isinstance(instance, Esylium) == True
