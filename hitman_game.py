from hitman import Hitman
import time


def main():
    print("hello world, let's play the hitman's game!")

    weak_hitman = Hitman("weak hitman")
    play_game(weak_hitman)

    magic_hitman = Hitman(name="magic hitman", has_magic=True)
    play_game(magic_hitman)

def play_game(hitman):
    print(hitman.name + "'s initial health is : " + str(hitman.health))

    while True:
        hitman.hit()
        # time.sleep(1)
        if not hitman.is_alive:
            break

    print(hitman.name + "is dead! game over! :(")


if __name__ == "__main__":
    main()
