"""Explorer agent type."""

from backend.agents.base import BaseAgent
import random
import numpy as np

class ExplorerAgent(BaseAgent):
    """Explorer agents that map and discover the world."""
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, agent_type="explorer")
        self.speed = 1.0
        self.max_energy = 150
        self.energy = 150
        self.visited_locations = set()
        self.discoveries = []
        self.exploration_radius = 50
    
    def decide_action(self):
        """Explorer decides where to explore."""
        if self.energy < 40:
            # Return to center
            self.move_towards(self.world.width / 2, self.world.height / 2)
        else:
            # Explore new areas
            self.explore()
    
    def explore(self):
        """Explore the world."""
        # Move towards unexplored areas
        target_x = random.uniform(0, self.world.width)
        target_y = random.uniform(0, self.world.height)
        self.move_towards(target_x, target_y)
        
        # Record visited location
        location = (int(self.x), int(self.y))
        if location not in self.visited_locations:
            self.visited_locations.add(location)
            discovery = {
                'location': location,
                'resources': random.randint(1, 10),
                'timestamp': self.age
            }
            self.discoveries.append(discovery)
            self.happiness += 5
    
    def step(self):
        """Execute one step."""
        super().step()
        self.happiness = 50 + len(self.discoveries)
