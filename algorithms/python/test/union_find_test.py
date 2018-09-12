
# Add the absolute paths to both the source and the test directories.
# This is a workaround needed to import the class to be tested
# without "ValueError: attempted relative import beyond top-level package".
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

from union_find import UnionFind

class UnionFindTest(unittest.TestCase):
    
    def test_smoke(self):
        union_find = UnionFind(5)
        union_find.union(1,2)

        self.assertTrue(union_find.connected(1,2))
        self.assertFalse(union_find.connected(0,1))

    def test_any_two_different_objects_disconnected_at_start(self):
        union_find = UnionFind(5)

        for i in range(4):
            for j in range(i+1,5):
                self.assertFalse(union_find.connected(i,j))

    def test_is_reflexive(self):
        union_find = UnionFind(5)

        for i in range(5):
            self.assertTrue(union_find.connected(i,i))

    def test_is_symmetric(self):
        union_find = UnionFind(5)
        union_find.union(1,2)

        self.assertTrue(union_find.connected(1,2))
        self.assertTrue(union_find.connected(2,1))
        self.assertFalse(union_find.connected(0,1))
        self.assertFalse(union_find.connected(1,0))

    def test_is_transitive(self):
        union_find = UnionFind(5)
        union_find.union(0,1)
        union_find.union(1,2)

        self.assertTrue(union_find.connected(0,2))

    def test_all_connections_and_properties_using_two_connected_components_with_five_objects(self):
        union_find = UnionFind(5)
        union_find.union(0,1)
        union_find.union(1,2)
        union_find.union(3,4)

        self.assertTrue(union_find.connected(0,0))
        self.assertTrue(union_find.connected(0,1))
        self.assertTrue(union_find.connected(0,2))
        self.assertFalse(union_find.connected(0,3))
        self.assertFalse(union_find.connected(0,4))

        self.assertTrue(union_find.connected(1,0))
        self.assertTrue(union_find.connected(1,1))
        self.assertTrue(union_find.connected(1,2))
        self.assertFalse(union_find.connected(1,3))
        self.assertFalse(union_find.connected(1,4))

        self.assertTrue(union_find.connected(2,0))
        self.assertTrue(union_find.connected(2,1))
        self.assertTrue(union_find.connected(2,2))
        self.assertFalse(union_find.connected(2,3))
        self.assertFalse(union_find.connected(2,4))

        self.assertFalse(union_find.connected(3,0))
        self.assertFalse(union_find.connected(3,1))
        self.assertFalse(union_find.connected(3,2))
        self.assertTrue(union_find.connected(3,3))
        self.assertTrue(union_find.connected(3,4))

        self.assertFalse(union_find.connected(4,0))
        self.assertFalse(union_find.connected(4,1))
        self.assertFalse(union_find.connected(4,2))
        self.assertTrue(union_find.connected(4,3))
        self.assertTrue(union_find.connected(4,4))

if __name__ == '__main__':
    unittest.main()