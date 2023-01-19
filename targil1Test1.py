import unittest
import targil1
import Targil1


class MyTestCase(unittest.TestCase):

    t=targil1.Targil1()
    def setUp(self):
        self.t.connect()

    def test_connect(self):
        self.assertEqual(self.t.connect(),1)

    def test_id(self):
       self.assertEqual(self.t.id('eli'),10)

    def test_order_sum(self):
       self.assertEqual(self.t.order_sum(self.t.order_list(self.t.id('eli'))),2578)

    def test_order_list(self):
        self.assertListEqual(self.t.order_list(10),[123, 2455])


if __name__ == '__main__':
    unittest.main()
