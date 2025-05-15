from interfaces.flower_controller import FlowerController

if __name__ == '__main__':
    fc = FlowerController()

    fc.create("Mawar", "Merah")
    fc.create("Melati", "Putih")

    for flower in fc.browse():
        print(f"{flower.name} berwarna {flower.description}")

    fc.update("Mawar", "Pink")
    print("Setelah update:")
    print(fc.read("Mawar").description)

    fc.delete("Melati")
    print("Setelah delete:")
    for flower in fc.browse():
        print(flower.name)
