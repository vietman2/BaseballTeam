from django.test import TestCase

# Create your tests here.
class Test(TestCase):
    # dummy to pass lint
    def test(self):
        self.assertEqual(1,1)

    def test1(self):
        self.assertEqual(1,2)
