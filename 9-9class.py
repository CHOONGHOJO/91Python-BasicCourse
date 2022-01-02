class Unit:
  def __init__(self):
    print("Unit 생성자")

class Flyable:
  def __init__(self):
    print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit):
  def __init__(self):
    # super().__init__() # 디중 상속시 맨 처음 class만 호출 상속됨 => 아래처럼 필요한것 다 init
    Unit.__init__(self)
    Flyable.__init__(self)

# drop ship
dropship = FlyableUnit()