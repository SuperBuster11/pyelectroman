import emdata as da

class EnemyData:
    def __init__(self):
        self.anims = {}
        self.frames = {}

class Enemies:
    def __init__(self):
        self.data = da.SpriteSet()
        self.data.load("enem")
        self.enemy = []
        self.enemy.append(EnemyData());
        self.enemy[0].anims["MLEFT"] = self.data.get_anim((0, 11))
        self.enemy[0].frames["MLEFT"] = len(self.enemy[0].anims["MLEFT"])
        self.enemy[0].anims["MRIGHT"] = self.data.get_anim((12, 22))
        self.enemy[0].frames["MRIGHT"] = len(self.enemy[0].anims["MRIGHT"])
        self.enemy[0].anims["SLEFT"] = self.data.get_anim((23, 23))
        self.enemy[0].frames["SLEFT"] = len(self.enemy[0].anims["SLEFT"])
        self.enemy[0].anims["SRIGHT"] = self.data.get_anim((24, 24))
        self.enemy[0].frames["SRIGHT"] = len(self.enemy[0].anims["SRIGHT"])
        self.enemy.append(EnemyData());
        self.enemy[1].anims["MLEFT"] = self.data.get_anim((32, 35))
        self.enemy[1].frames["MLEFT"] = len(self.enemy[1].anims["MLEFT"])
        self.enemy[1].anims["MRIGHT"] = self.data.get_anim((36, 39))
        self.enemy[1].frames["MRIGHT"] = len(self.enemy[1].anims["MRIGHT"])
        self.enemy[1].anims["SLEFT"] = self.data.get_anim((40, 40))
        self.enemy[1].frames["SLEFT"] = len(self.enemy[1].anims["SLEFT"])
        self.enemy[1].anims["SRIGHT"] = self.data.get_anim((41, 41))
        self.enemy[1].frames["SRIGHT"] = len(self.enemy[1].anims["SRIGHT"])
        self.enemy.append(EnemyData());
        self.enemy[2].anims["MLEFT"] = self.data.get_anim((42, 42))
        self.enemy[2].frames["MLEFT"] = len(self.enemy[2].anims["MLEFT"])
        self.enemy[2].anims["MRIGHT"] = self.data.get_anim((43, 43))
        self.enemy[2].frames["MRIGHT"] = len(self.enemy[2].anims["MRIGHT"])
        self.enemy[2].anims["SLEFT"] = self.data.get_anim((44, 44))
        self.enemy[2].frames["SLEFT"] = len(self.enemy[2].anims["SLEFT"])
        self.enemy[2].anims["SRIGHT"] = self.data.get_anim((44, 44))
        self.enemy[2].frames["SRIGHT"] = len(self.enemy[2].anims["SRIGHT"])
        self.enemy.append(EnemyData());
        self.enemy[3].anims["MLEFT"] = self.data.get_anim((48, 51))
        self.enemy[3].frames["MLEFT"] = len(self.enemy[3].anims["MLEFT"])
        self.enemy[3].anims["MRIGHT"] = self.data.get_anim((52, 55))
        self.enemy[3].frames["MRIGHT"] = len(self.enemy[3].anims["MRIGHT"])
        self.enemy[3].anims["SLEFT"] = self.data.get_anim((56, 56))
        self.enemy[3].frames["SLEFT"] = len(self.enemy[3].anims["SLEFT"])
        self.enemy[3].anims["SRIGHT"] = self.data.get_anim((57, 57))
        self.enemy[3].frames["SRIGHT"] = len(self.enemy[3].anims["SRIGHT"])

    def get_anims(self, enemy_num):
        return (self.enemy[enemy_num].anims,
                self.enemy[enemy_num].frames)

class Weapons:
    def __init__(self):
        self.data = da.SpriteSet()
        self.data.load("weapons")

# -----------------------------------------------------------------------------
# test code below

def main():
    pass

if __name__ == "__main__":
    main()
