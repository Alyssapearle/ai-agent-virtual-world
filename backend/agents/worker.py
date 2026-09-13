"""Worker agent type."""

from backend.agents.base import BaseAgent
import random
import numpy as np

class WorkerAgent(BaseAgent):
    """Worker agents that gather resources and produce goods."""
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, agent_type="worker")
        self.speed = 0.5
        self.max_energy = 100
        self.energy = 100
        self.carrying_capacity = 10
        self.current_load = 0
        self.resource_type = None
        self.work_efficiency = 0.8 + random.uniform(-0.1, 0.1)
    
    def decide_action(self):
        """Worker decides to gather resources or move."""
        if self.energy < 30:
            # Find rest area
            self.move_randomly()
        elif self.current_load >= self.carrying_capacity:
            # Go to dropoff point
            self.move_towards(self.world.width / 2, self.world.height / 2)
        else:
            # Search for resources
            self.search_for_resources()
    
    def search_for_resources(self):
        """Search for resources in the world."""
        # Simulate resource gathering
        if random.random() < 0.2:  # 20% chance per step
            self.gather_resource()
        else:
            self.move_randomly()
    
    def gather_resource(self):
        """Gather a resource."""
        if self.current_load < self.carrying_capacity:
            amount = random.uniform(0.5, 2.0) * self.work_efficiency
            self.current_load += amount
            self.energy -= 5  # Energy cost
            self.inventory['resources'] = self.inventory.get('resources', 0) + amount
    
    def step(self):
        """Execute one step."""
        super().step()
        self.happiness = 50 + (self.current_load * 5)
