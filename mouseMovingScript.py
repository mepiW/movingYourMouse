import mouse, random, time

def main():
    while True:
        randomX = random.randint(-960, 960)
        randomY = random.randint(-540, 540)
        randomDuration = random.randint(7, 15)

        time.sleep(random.randint(0, 5))
        
        mouse.move(randomX, randomY, absolute = False, duration = randomDuration/10)

        print(f"Moving mouse to: {randomX}, {randomY}")

main()