# -*- coding: utf-8 -*-
import unittest
from .gilded_rose import Item, GildedRose, GeneralItem, AgedBrieItem, ConcertItem, LegendaryItem


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


class GildedGeneralItemTest(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_general_item_decrease_by_one(self):
        self.items.append(
            GeneralItem(
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
            GeneralItem(
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
            GeneralItem(
                name="NormalItemCaseAlwaysPositive",
                sell_in=10,
                quality=0))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 0)


class AgedBrieItemTest(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_aged_brie_item_quality_increases(self):
        self.items.append(
            AgedBrieItem(
                name="Aged Brie",
                sell_in=10,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

    def test_aged_brie_item_quality_no_more_than_50(self):
        self.items.append(
            AgedBrieItem(
                name="Aged Brie",
                sell_in=10,
                quality=49))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 8)
        self.assertEqual(item.quality, 50)

    def test_aged_brie_item_quality_double_increase(self):
        self.items.append(
            AgedBrieItem(
                name="Aged Brie",
                sell_in=1,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 23)


class LegendaryItemTest(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_legendary_item_quality_does_not_change(self):
        self.items.append(
            LegendaryItem(
                name="Sulfuras, Hand of Ragnaros",
                sell_in=10))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 80)


class ConcertItemTest(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_concert_item_quality_increases(self):
        self.items.append(
            ConcertItem(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=15,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_concert_item_quality_increases_by_two(self):
        self.items.append(
            ConcertItem(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=10,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_concert_item_quality_increases_by_three(self):
        self.items.append(
            ConcertItem(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=5,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_concert_item_quality_goes_to_zero_after_concert(self):
        self.items.append(
            ConcertItem(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=1,
                quality=20))

        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

        self.assertEqual(len(self.items), 1)
        item = self.items[0]

        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 23)

        gilded_rose.update_quality()

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
