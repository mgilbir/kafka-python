from testutil import *
from mock import MagicMock, patch
from kafka.consumer import SimpleConsumer

class TestKafkaConsumer(KafkaTestCase):
    def test_non_integer_partitions(self):
        with self.assertRaises(AssertionError):
            consumer = SimpleConsumer(MagicMock(), 'group', 'topic', partitions = [ '0' ])
