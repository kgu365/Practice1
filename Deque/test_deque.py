from deque import Deque
import unittest

class TestDequeMethods(unittest.TestCase):
   def test_init(self):
      x = Deque()
      self.assertTrue(x.get_size() == 0)

   def test_isEmpty(self):
      x = Deque()
      self.assertTrue(x.isEmpty())

   def test_addFirstToEmpyList(self):
      x = Deque()
      x.addFirst(1)
      self.assertFalse(x.isEmpty())
      self.assertTrue(x.removeFirst() == 1)

   def test_addFirst(self):
      x = Deque()
      x.addFirst(1)
      x.addFirst(2)
      self.assertTrue(x.removeFirst() == 2)
      self.assertTrue(x.removeFirst() == 1)

   def test_addLast(self):
      x = Deque()
      x.addLast(1)
      x.addLast(2)
      self.assertTrue(x.removeLast() == 2)
      self.assertTrue(x.removeLast() == 1)

   def test_addLastToEmptyList(self):
      x = Deque()
      x.addLast(2)
      self.assertFalse(x.isEmpty())
      self.assertTrue(x.removeLast() == 2)

   def test_removeFirst(self):
      x = Deque()
      x.addFirst(1)
      x.addLast(2)
      self.assertTrue(x.get_size() == 2)
      item = x.removeFirst()
      self.assertTrue(item == 1)

   def test_removeLast(self):
      x = Deque()
      x.addFirst(1)
      x.addFirst(0)
      x.addLast(2)
      x.addLast(3)
      self.assertEqual(x.get_size(), 4)
      item = x.removeLast()
      self.assertEqual(item, 3)
      item = x.removeLast()
      self.assertEqual(item, 2)
      item = x.removeLast()
      self.assertEqual(item, 1)
      item = x.removeLast()
      self.assertEqual(item, 0)

   def test_removeEmpty(self):
      x = Deque()
      self.assertEqual(x.removeFirst(), None)
      self.assertEqual(x.removeLast(), None)

   def test_iterator(self):
      x = Deque()
      x.addFirst(3)
      x.addFirst(2)
      x.addFirst(1)
      it = x.iterator()
      num = 1
      for x in it:
         self.assertEqual(num, x)
         num += 1

if __name__ == '__main__':
   unittest.main()
