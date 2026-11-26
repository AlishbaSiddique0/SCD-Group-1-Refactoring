class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def _increase_quality(self, item, amount=1):
        item.quality = min(self.MAX_QUALITY, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(self.MIN_QUALITY, item.quality - amount)

    def _update_aged_brie(self, item):
        self._increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._increase_quality(item)

    def _update_backstage_pass(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = self.MIN_QUALITY

    def _update_normal_item(self, item):
        self._decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._decrease_quality(item)

    def _update_single_item(self, item):
        if item.name == self.SULFURAS:
            return
        if item.name == self.AGED_BRIE:
            self._update_aged_brie(item)
            return
        if item.name == self.BACKSTAGE_PASS:
            self._update_backstage_pass(item)
            return
        self._update_normal_item(item)

    def update_quality(self):
        for item in self.items:
            self._update_single_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
