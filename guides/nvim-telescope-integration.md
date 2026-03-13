# Using Neovim Telescope to Search Cheatsheets

This guide explains how to configure [nvim-telescope](https://github.com/nvim-telescope/telescope.nvim) to search over all the cheatsheet files in this repository.

## Prerequisites

- [Neovim](https://neovim.io/) 0.9+
- [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)
- [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) for live grep support

## Installation

### Using lazy.nvim

```lua
{
  "nvim-telescope/telescope.nvim",
  dependencies = { "nvim-lua/plenary.nvim" },
}
```

### Using packer.nvim

```lua
use {
  "nvim-telescope/telescope.nvim",
  requires = { "nvim-lua/plenary.nvim" },
}
```

## Searching the Cheatsheets

### Option 1: Live Grep (search by content)

Open a terminal in the directory where the cheatsheet files are cloned, then launch Neovim and run:

```vim
:lua require("telescope.builtin").live_grep({ cwd = "/path/to/cheatsheet" })
```

This lets you search the full text of every cheatsheet file in real time.

### Option 2: Find Files (search by filename)

```vim
:lua require("telescope.builtin").find_files({ cwd = "/path/to/cheatsheet" })
```

### Option 3: Custom keymaps

Add the following to your Neovim config (`init.lua`) to bind dedicated shortcuts:

```lua
local cheatsheet_dir = "/path/to/cheatsheet"

vim.keymap.set("n", "<leader>cs", function()
  require("telescope.builtin").live_grep({ cwd = cheatsheet_dir, prompt_title = "Search Cheatsheets" })
end, { desc = "Search cheatsheet content" })

vim.keymap.set("n", "<leader>cf", function()
  require("telescope.builtin").find_files({ cwd = cheatsheet_dir, prompt_title = "Find Cheatsheet" })
end, { desc = "Find cheatsheet file" })
```

Replace `/path/to/cheatsheet` with the actual path where this repository is cloned (e.g. `~/projects/cheatsheet`).

## Telescope UI Tips

| Key | Action |
| --- | --- |
| `<C-n>` / `<C-p>` | Move to next / previous result |
| `<CR>` | Open selected file |
| `<C-x>` | Open in horizontal split |
| `<C-v>` | Open in vertical split |
| `<C-t>` | Open in new tab |
| `<Esc>` / `<C-c>` | Close Telescope |

## Filtering to Markdown Files Only

To limit results to `.md` files when using live grep:

```lua
require("telescope.builtin").live_grep({
  cwd = "/path/to/cheatsheet",
  glob_pattern = "*.md",
  prompt_title = "Search Cheatsheets",
})
```
