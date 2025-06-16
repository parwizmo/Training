import asyncio
import platform
from wumpus_mdp import WumpusWorldMDP
from graphics.wumpus_gui import WumpusWorld, update_loop, pygame


async def main():
    GRID_SIZE = 4
    custom_map = True

    # for testing
    # Set custom_map to False to generate random map
    mdp = WumpusWorldMDP(size=GRID_SIZE, custom_map=custom_map)

    # TODO --- Uncomment the pair of lines below to enable execution of each algorithm ---

    # --- 1. Policy Iteration ---
    algorithm_name = "PI"
    policy, values = mdp.policy_iteration()

    # --- 2. Value Iteration ---
    # algorithm_name = 'VI'
    # policy, values = mdp.value_iteration()

    game = WumpusWorld(mdp, policy, algorithm_name)
    while True:
        continue_running = await update_loop(game)
        if not continue_running:
            break
        await asyncio.sleep(1.0 / 60)  # 60 FPS

    pygame.quit()
    exit()


if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        try:
            asyncio.run(main())
        except Exception as e:
            print(f"Main loop error: {e}")
