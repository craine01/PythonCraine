def love(beat):
    if beat <= 0:
            print("You're cooked")
            return
    else:
        print(f"Your love smells stinky as number: {beat}")
        love(beat-1)
love(3)