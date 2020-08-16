# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Until Convince Goblin to share ownership of Item Class
            if hasattr(item, 'update_item'):
                item.update_item()
            else:
                if item.name == 'Aged Brie':
                    item = AgedBrieItem(
                        name=item.name,
                        sell_in=item.sell_in,
                        quality=item.quality
                    )
                    item.update_item()
                elif item.name == 'Sulfuras, Hand of Ragnaros':
                    item = LegendaryItem(
                        name=item.name,
                        sell_in=item.sell_in,
                    )
                    item.update_item()
                elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                    item = ConcertItem(
                        name=item.name,
                        sell_in=item.sell_in,
                        quality=item.quality
                    )
                    item.update_item()
                else:
                    item = GeneralItem(
                        name=item.name,
                        sell_in=item.sell_in,
                        quality=item.quality
                    )
                    item.update_item()


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
