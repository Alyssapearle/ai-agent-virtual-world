# 🌍 AI Agent Virtual World

A comprehensive simulation platform featuring autonomous AI agents with learning capabilities, social interactions, economic systems, and real-time 3D visualization.

## Features

✨ **Core Capabilities**
- **Autonomous Agents**: Self-governing AI entities with goals, behaviors, and learning
- **Multi-Agent Interactions**: Communication, cooperation, competition, and trade
- **Learning Systems**: Reinforcement learning, neural networks, genetic algorithms
- **Economic Simulation**: Markets, trading, resource management
- **Social Dynamics**: Relationships, hierarchies, group behaviors
- **3D Environment**: Real-time Babylon.js visualization
- **Scalability**: Support for thousands of concurrent agents
- **Research-Ready**: Extensible for custom simulations

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Alyssapearle/ai-agent-virtual-world.git
cd ai-agent-virtual-world

# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd web
npm install
cd ..
```

### Running the Simulation

```bash
# Start the backend server
python main.py

# In another terminal, start the frontend
cd web
npm start
```

Visit `http://localhost:3000` to see the simulation in action!

## Project Structure

```
ai-agent-virtual-world/
├── backend/
│   ├── agents/              # Agent classes and behaviors
│   ├── world/               # World simulation engine
│   ├── learning/            # ML/RL systems
│   ├── economics/           # Market and trading systems
│   ├── communication/       # Agent messaging
│   └── utils/              # Utilities and helpers
├── web/
│   ├── public/             # Static assets
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── scenes/         # Babylon.js scenes
│   │   └── utils/          # Frontend utilities
│   └── package.json
├── simulations/            # Example simulations
├── docs/                   # Documentation
├── tests/                  # Test suite
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point
└── README.md
```

## Use Cases

### 🔬 Research & Academia
- Multi-agent systems research
- Emergence and complexity studies
- Economic modeling
- Social behavior simulation

### 🎮 Entertainment & Games
- Interactive AI-driven worlds
- Procedural storytelling
- Dynamic NPC populations
- Emergent gameplay

### 📚 Education
- Teaching AI/ML concepts
- Agent-based modeling
- Complex systems
- Programming practices

## Agent Types

| Type | Purpose | Capabilities |
|------|---------|--------------|
| **Worker** | Task completion | Pathfinding, resource gathering, production |
| **Trader** | Commerce | Negotiation, pricing, market analysis |
| **Explorer** | Discovery | Mapping, information gathering |
| **Learner** | Adaptation | Neural networks, reinforcement learning |
| **Social** | Relationships | Cooperation, hierarchy, communication |
| **Custom** | User-defined | Extensible framework |

## Configuration

Edit `config.yaml` to customize:
- World size and complexity
- Agent count and types
- Learning algorithms
- Simulation speed
- Visualization options

## Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Agent Development](docs/agent-development.md)
- [API Reference](docs/api-reference.md)
- [Simulation Examples](docs/examples.md)
- [Architecture Overview](docs/architecture.md)

## API Examples

### Python Backend

```python
from backend.world import World
from backend.agents import Agent

# Create world
world = World(width=100, height=100, num_agents=50)

# Run simulation
for step in range(1000):
    world.step()
    stats = world.get_statistics()
    print(f"Step {step}: {len(world.agents)} agents")
```

### REST API

```bash
# Get world state
curl http://localhost:5000/api/world/state

# Get agent info
curl http://localhost:5000/api/agents/1

# Run simulation step
curl -X POST http://localhost:5000/api/world/step

# Get statistics
curl http://localhost:5000/api/world/stats
```

## Development

### Adding New Agent Types

```python
from backend.agents import BaseAgent

class CustomAgent(BaseAgent):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.custom_property = "value"
    
    def step(self):
        # Define behavior for each simulation step
        self.move_randomly()
        self.interact_with_neighbors()
```

### Creating Simulations

See `simulations/` directory for examples:
- `basic_economy.py` - Trading and markets
- `social_network.py` - Relationship dynamics
- `learning_agents.py` - Neural network training
- `emergent_behavior.py` - Complexity and emergence

## Performance

- **Baseline**: 1,000 agents @ 30 FPS
- **Optimized**: 10,000+ agents @ 10 FPS
- **Headless mode**: 100,000+ agents for research

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Citation

If you use this in research, please cite:

```bibtex
@software{aivw2024,
  title={AI Agent Virtual World},
  author={Your Name},
  year={2024},
  url={https://github.com/Alyssapearle/ai-agent-virtual-world}
}
```

## Support & Community

- 📖 [Documentation](docs/)
- 💬 [Discussions](https://github.com/Alyssapearle/ai-agent-virtual-world/discussions)
- 🐛 [Issues](https://github.com/Alyssapearle/ai-agent-virtual-world/issues)
- 📧 Contact: [your-email@example.com]

---

**Made with ❤️ for AI researchers, game developers, and AI enthusiasts**
