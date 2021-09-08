import unittest

from ..utils import TranspileTestCase

class MathModuleTests(TranspileTestCase):
    def test_fabs(self):
        self.assertCodeExecution("""
            import math
            print(math.fabs(10234))
            print(math.fabs(0.0001))
            print(math.fabs(0))
            print(math.fabs(-1))
            """)
    @unittest.expectedFailure    
    def test_fail(self):
        self.assertCodeExecution("""
            import math 
            try:
                print(math.fabs('12334'))
            except Exception as e:
                print(type(e), e)
            """)