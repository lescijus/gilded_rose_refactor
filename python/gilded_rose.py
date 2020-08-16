# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GeneralItem(Item):

    def update_item(self):
        self.update_quality()
        self.update_sell_in()

    def update_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality = self.quality - 1


class AgedBrieItem(Item):

    def update_item(self):
        self.update_quality()
        self.update_sell_in()

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality = self.quality + 1


class LegendaryItem(Item):
    def __init__(self, name, sell_in):
        super().__init__(name, sell_in, 80)

    def update_item(self):
        pass


class ConcertItem(Item):

    def update_item(self):
        self.update_quality()
        self.update_sell_in()

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        if self.sell_in < 11 and self.quality < 50:
            self.quality = self.quality + 1
        if self.sell_in < 6 and self.quality < 50:
            self.quality = self.quality + 1

    def update_sell_in(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0
