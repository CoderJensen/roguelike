from __future__ import annotations

import tcod.context
import tcod.tileset

def main() -> None:
    """Load a tileset and open a window using it, this window will immediately close."""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    with tcod.context.new(tileset=tileset) as context:
        # The window will stay open for the duration of the block
        pass

if __name__ == "__main__":
    main()