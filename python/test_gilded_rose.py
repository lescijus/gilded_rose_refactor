# -*- coding: utf-8 -*-
import unittest
from .gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


class GildedGeneralItem(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_general_item_decrease_by_one(self):
        self.items.append(
            Item(
                name="NormalItemCaseNormal",
                sell_in=10,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    def test_general_item_decrease_is_double(self):
        self.items.append(
            Item(
                name="NormalItemCaseDouble",
                sell_in=0,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 18)

    def test_general_item_quality_is_always_positive(self):
        self.items.append(
            Item(
                name="NormalItemCaseAlwaysPositive",
                sell_in=10,
                quality=0))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 0)

    def test_general_item_quality_is_always_positive2(self):
        self.items.append(
            Item(
                name="NormalItemCaseAlwaysPositive",
                sell_in=0,
                quality=1))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
