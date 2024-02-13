class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        targets_distance = abs(abs(target[0]) + abs(target[1])) # compute manhattan distance from the origin(where you start)

        # Loop through ghosts list to find the manhattan distance of a ghost from target and compare it with the manhattand distance of the orgin and the target
        for ghost in ghosts:
            manhattan_distance = (abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
            if manhattan_distance <= targets_distance:
                return False
        
        return True