"""Base agent class."""

import random
import uuid
from typing import Dict, List, Tuple
import numpy as np

class BaseAgent:
    """Base class for all agents in the world."""
    
    def __init__(self, world, x: float, y: float, agent_type: str = "base"):
        self.id = str(uuid.uuid4())[:8]
        self.world = world
        self.x = x
        self.y = y
        self.agent_type = agent_type
        
        # Energy system
        self.energy = 100
        self.max_energy = 100
        self.energy_decay = 0.1  # Energy lost per step
        
        # Behavior
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 0.5
        
        # State
        self.state = "idle"
        self.goal = None
        self.inventory = {}
        
        # Social
        self.relationships = {}
        self.happiness = 50
        self.age = 0
        
        # Learning
        self.memory = []
        self.neural_network = None
        self.q_table = {}  # For Q-learning
    
    def step(self):
        """Execute one step of the agent."""
        self.age += 1
        self.update_energy()
        self.update_position()
        self.interact()
        self.decide_action()
    
    def update_energy(self):
        """Update agent's energy."""
        self.energy -= self.energy_decay
        self.energy = max(0, min(self.energy, self.max_energy))
        
        # Death if no energy
        if self.energy <= 0:
            self.state = "dead"
    
    def update_position(self):
        """Update agent's position based on velocity."""
        self.x += self.velocity_x * self.speed
        self.y += self.velocity_y * self.speed
        
        # Boundary wrapping
        self.x = self.x % self.world.width
        self.y = self.y % self.world.height
        
        # Reset velocity
        self.velocity_x = 0
        self.velocity_y = 0
    
    def move_towards(self, target_x: float, target_y: float):
        """Move towards a target position."""
        dx = target_x - self.x
        dy = target_y - self.y
        distance = np.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.velocity_x = dx / distance
            self.velocity_y = dy / distance
    
    def move_randomly(self):
        """Move in a random direction."""
        angle = random.uniform(0, 2 * np.pi)
        self.velocity_x = np.cos(angle)
        self.velocity_y = np.sin(angle)
    
    def get_nearby_agents(self, radius: float = 10) -> List['BaseAgent']:
        """Get agents within a radius."""
        nearby = []
        for agent in self.world.agents:
            if agent.id != self.id:
                distance = np.sqrt((self.x - agent.x)**2 + (self.y - agent.y)**2)
                if distance < radius:
                    nearby.append((agent, distance))
        return nearby
    
    def interact(self):
        """Interact with nearby agents."""
        nearby = self.get_nearby_agents(radius=5)
        for agent, distance in nearby:
            if random.random() < 0.1:  # 10% chance to interact
                self.communicate(agent)
    
    def communicate(self, other_agent: 'BaseAgent'):
        """Communicate with another agent."""
        # Store interaction in memory
        self.memory.append({
            'agent_id': other_agent.id,
            'type': other_agent.agent_type,
            'distance': np.sqrt((self.x - other_agent.x)**2 + (self.y - other_agent.y)**2),
            'timestamp': self.age
        })
        
        # Update relationships
        if other_agent.id not in self.relationships:
            self.relationships[other_agent.id] = 0
        self.relationships[other_agent.id] += random.uniform(-5, 5)
    
    def decide_action(self):
        """Decide what action to take."""
        # Default: random movement
        self.move_randomly()
    
    def get_state(self) -> Dict:
        """Get agent's current state."""
        return {
            'id': self.id,
            'type': self.agent_type,
            'x': self.x,
            'y': self.y,
            'energy': self.energy,
            'happiness': self.happiness,
            'age': self.age,
            'state': self.state,
            'inventory': self.inventory,
            'relationships': len(self.relationships)
        }
    
    def reward(self, amount: float):
        """Give reward to agent."""
        self.energy = min(self.energy + amount, self.max_energy)
        self.happiness = min(self.happiness + amount / 2, 100)
    
    def punish(self, amount: float):
        """Punish agent."""
        self.energy = max(self.energy - amount, 0)
        self.happiness = max(self.happiness - amount / 2, 0)
