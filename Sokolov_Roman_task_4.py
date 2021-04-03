class Storage:
    def __init__(self, volume):
        self.volume = volume


class OfficeEquipment:
    def __init__(self, volume, brand):
        self.volume = volume
        self.brand = brand


class Printer(OfficeEquipment):
    def __init__(self, volume, brand, cartridge_type):
        super().__init__(volume, brand)
        self.cartridge_type = cartridge_type


class Scanner(OfficeEquipment):
    def __init__(self, volume, brand, ):