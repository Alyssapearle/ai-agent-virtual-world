#!/usr/bin/env python3
"""
Main entry point for AI Agent Virtual World simulation.
"""

import sys
import argparse
from backend.world import World
from backend.api import create_app

def run_simulation(config_path=None, headless=False, port=5000):
    """Run the simulation."""
    print("🌍 Initializing AI Agent Virtual World...")
    
    # Create world
    world = World(config_path=config_path)
    
    if headless:
        print(f"🚀 Running headless simulation with {len(world.agents)} agents")
        # Run without visualization
        try:
            for step in range(10000):
                world.step()
                if step % 100 == 0:
                    stats = world.get_statistics()
                    print(f"Step {step}: {len(world.agents)} agents | Avg happiness: {stats.get('avg_happiness', 0):.2f}")
        except KeyboardInterrupt:
            print("\n⏹️  Simulation stopped")
    else:
        print(f"🚀 Starting API server on port {port}")
        app = create_app(world)
        app.run(debug=True, port=port, use_reloader=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Agent Virtual World")
    parser.add_argument("--config", type=str, help="Path to config file")
    parser.add_argument("--headless", action="store_true", help="Run without visualization")
    parser.add_argument("--port", type=int, default=5000, help="API server port")
    
    args = parser.parse_args()
    run_simulation(args.config, args.headless, args.port)
