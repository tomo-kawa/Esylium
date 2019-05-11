import pytest
from src import Esylium

class TestEsylium(object):

    @pytest.fixture
    def instance():
        return Esylium()

    def test_constract(instance):
        assert instance == object
