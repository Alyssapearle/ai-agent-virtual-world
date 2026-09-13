"""Learner agent type with neural network capabilities."""

from backend.agents.base import BaseAgent
import random
import numpy as np

class LearnerAgent(BaseAgent):
    """Learning agents that adapt using neural networks."""
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, agent_type="learner")
        self.speed = 0.3
        self.max_energy = 100
        self.energy = 100
        self.learning_rate = 0.1
        self.experiences = []
        self.knowledge = {}
        self.intelligence = 0.5 + random.uniform(-0.1, 0.2)
    
    def decide_action(self):
        """Learner uses accumulated knowledge to decide."""
        if len(self.experiences) > 0:
            # Learn from past experiences
            self.learn_from_experience()
        else:
            # Explore
            self.move_randomly()
    
    def learn_from_experience(self):
        """Learn from stored experiences."""
        if self.experiences:
            recent = self.experiences[-5:]
            for exp in recent:
                state = exp.get('state', {})
                action = exp.get('action', '')
                reward = exp.get('reward', 0)
                
                # Simple learning: track successful actions
                key = str(state)
                if key not in self.knowledge:
                    self.knowledge[key] = {}
                
                if action not in self.knowledge[key]:
                    self.knowledge[key][action] = 0
                
                self.knowledge[key][action] += reward * self.learning_rate
            
            # Use best known action
            if self.knowledge:
                best_action = random.choice(list(self.knowledge.values()))[0]
                if best_action == 'move':
                    self.move_randomly()
    
    def record_experience(self, state, action, reward):
        """Record an experience for learning."""
        self.experiences.append({
            'state': state,
            'action': action,
            'reward': reward,
            'timestamp': self.age
        })
    
    def step(self):
        """Execute one step."""
        super().step()
        self.happiness = 50 + len(self.knowledge) * 5
