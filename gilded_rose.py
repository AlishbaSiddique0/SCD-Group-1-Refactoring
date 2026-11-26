class ItemUpdater:
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, item):
        self.item = item

    def increase_quality(self, amount=1):
        self.item.quality = min(self.MAX_QUALITY, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        self.item.quality = max(self.MIN_QUALITY, self.item.quality - amount)

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update(self):
        raise NotImplementedError("Subclasses must implement update()")


class NormalItemUpdater(ItemUpdater):
    def update(self):
        self.update_sell_in()
        decrement = 2 if self.item.sell_in < 0 else 1
        self.decrease_quality(decrement)


class AgedBrieUpdater(ItemUpdater):
    def update(self):
        self.update_sell_in()
        increment = 2 if self.item.sell_in < 0 else 1
        self.increase_quality(increment)


class BackstagePassUpdater(ItemUpdater):
    def update(self):
        if self.item.sell_in <= 0:
            self.update_sell_in()
            self.item.quality = self.MIN_QUALITY
            return
        increment = 3 if self.item.sell_in < 6 else (2 if self.item.sell_in < 11 else 1)
        self.increase_quality(increment)
        self.update_sell_in()


class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass


class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    UPDATER_MAP = {
        AGED_BRIE: AgedBrieUpdater,
        BACKSTAGE_PASS: BackstagePassUpdater,
        SULFURAS: SulfurasUpdater,
    }

    def __init__(self, items):
        self.items = items

    def _create_updater(self, item):
        updater_cls = self.UPDATER_MAP.get(item.name, NormalItemUpdater)
        return updater_cls(item)

    def update_quality(self):
        for item in self.items:
            updater = self._create_updater(item)
            updater.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
