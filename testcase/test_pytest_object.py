import logging


class TestPytestObject:
    logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def setup_class(cls):
        logging.info("setup_class")

    def setup_method(self):
        logging.info("setup")

    def test_two(self):
        assert 1 == 2

    def test_one(self):
        assert True == False

    def teardown_method(self):
        logging.info("teardown")

    @classmethod
    def teardown_method(cls):
        logging.info("teardown_class")
