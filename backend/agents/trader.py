"""Trader agent type."""

from backend.agents.base import BaseAgent
import random
import numpy as np

class TraderAgent(BaseAgent):
    """Trader agents that buy and sell goods."""
    
    def __init__(self, world, x, y):
        super().__init__(world, x, y, agent_type="trader")
        self.speed = 0.7
        self.max_energy = 120
        self.energy = 120
        self.capital = 1000
        self.inventory_value = 0
        self.profit_history = []
        self.trade_skill = 0.7 + random.uniform(-0.1, 0.2)
    
    def decide_action(self):
        """Trader decides to buy, sell, or move."""
        if random.random() < 0.3:  # 30% chance to engage in trade
            self.attempt_trade()
        else:
            self.move_randomly()
    
    def attempt_trade(self):
        """Attempt to trade with nearby agents."""
        nearby = self.get_nearby_agents(radius=10)
        if nearby:
            other_agent, distance = random.choice(nearby)
            if hasattr(other_agent, 'inventory') and other_agent.inventory:
                self.execute_trade(other_agent)
    
    def execute_trade(self, other_agent):
        """Execute trade with another agent."""
        if random.random() < self.trade_skill:
            # Profitable trade
            profit = random.uniform(10, 50) * self.trade_skill
            self.capital += profit
            other_agent.capital = getattr(other_agent, 'capital', 0) - profit / 2
            self.profit_history.append(profit)
            self.energy -= 2
    
    def step(self):
        """Execute one step."""
        super().step()
        avg_profit = np.mean(self.profit_history[-10:]) if self.profit_history else 0
        self.happiness = 50 + (avg_profit / 10)
