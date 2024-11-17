import unittest

SERVER = "server_a"

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual('hola', 'hola')
        
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)
        
    def test_asser_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")
            
    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(7, [2, 4, 5, 10])
        
    def test_assert_dicts(self):
        user = {'first_name': 'Pedro', 'second_name': 'Perez'}
        self.assertDictEqual(
            {'first_name': 'Pedro', 'second_name': 'Perez'},
            user
        )
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )

    @unittest.skip('Trabajo en progreso')
    def test_skip(self):
        self.assertEqual(10,10)
        
    @unittest.skipIf(SERVER == "server_a", "saltada por que no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(10,10)
        
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)