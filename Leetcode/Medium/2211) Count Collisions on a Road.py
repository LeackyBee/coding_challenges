class Solution:
    def countCollisions(self, directions: str) -> int:
        output = 0
        trailing_rs = 0
        directions = list(directions)
        for i in range(len(directions) - 1):
            print(directions[i] + directions[i + 1])
            match directions[i] + directions[i + 1]:
                case "RL":
                    output += 2 + trailing_rs
                    trailing_rs = 0
                    directions[i + 1] = "S"  # can set this to stationary so that next car collides
                case "SL":
                    output += 1
                    directions[i + 1] = "S"  # can set this to stationary so that next car collides
                case "RS":
                    output += 1 + trailing_rs
                    trailing_rs = 0
                case _:
                    # no collision, so track if we're moving on from an R
                    if directions[i] == "R":
                        trailing_rs += 1

        return output
