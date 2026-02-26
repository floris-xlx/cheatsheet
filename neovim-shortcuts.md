# Neovim Shortcuts

> **Note:** `<leader>` is typically mapped to `\` or `,` by the user. Modes: **N** = Normal, **I** = Insert, **V** = Visual, **C** = Command.

## Modes

| Shortcut | Action | Mode |
| --- | --- | --- |
| i | Enter Insert mode (before cursor) | N |
| I | Enter Insert mode (beginning of line) | N |
| a | Enter Insert mode (after cursor) | N |
| A | Enter Insert mode (end of line) | N |
| o | Open new line below and enter Insert mode | N |
| O | Open new line above and enter Insert mode | N |
| s | Delete character and enter Insert mode | N |
| S | Delete line and enter Insert mode | N |
| c | Change (delete then insert) | N |
| C | Change to end of line | N |
| R | Enter Replace mode | N |
| v | Enter Visual mode (character) | N |
| V | Enter Visual Line mode | N |
| Ctrl + v | Enter Visual Block mode | N |
| : | Enter Command-line mode | N |
| / | Enter search (forward) | N |
| ? | Enter search (backward) | N |
| Esc | Return to Normal mode | I/V/C |
| Ctrl + [ | Return to Normal mode | I/V/C |
| Ctrl + c | Return to Normal mode | I |

## Navigation

| Shortcut | Action | Mode |
| --- | --- | --- |
| h | Move left | N/V |
| j | Move down | N/V |
| k | Move up | N/V |
| l | Move right | N/V |
| w | Jump forward to start of word | N/V |
| W | Jump forward to start of WORD | N/V |
| b | Jump backward to start of word | N/V |
| B | Jump backward to start of WORD | N/V |
| e | Jump forward to end of word | N/V |
| E | Jump forward to end of WORD | N/V |
| ge | Jump backward to end of word | N/V |
| 0 | Move to beginning of line | N/V |
| ^ | Move to first non-blank character of line | N/V |
| $ | Move to end of line | N/V |
| g_ | Move to last non-blank character of line | N/V |
| gg | Move to first line of file | N/V |
| G | Move to last line of file | N/V |
| {number}G | Move to line number | N |
| {number}gg | Move to line number | N |
| H | Move to top of visible screen | N |
| M | Move to middle of visible screen | N |
| L | Move to bottom of visible screen | N |
| Ctrl + d | Scroll half page down | N |
| Ctrl + u | Scroll half page up | N |
| Ctrl + f | Scroll full page down | N |
| Ctrl + b | Scroll full page up | N |
| Ctrl + e | Scroll one line down | N |
| Ctrl + y | Scroll one line up | N |
| zz | Center cursor on screen | N |
| zt | Move cursor to top of screen | N |
| zb | Move cursor to bottom of screen | N |
| % | Jump to matching bracket | N |
| f{char} | Jump forward to character | N/V |
| F{char} | Jump backward to character | N/V |
| t{char} | Jump forward before character | N/V |
| T{char} | Jump backward before character | N/V |
| ; | Repeat last f/F/t/T | N |
| , | Repeat last f/F/t/T in reverse | N |
| ' + {mark} | Jump to line of mark | N |
| \` + {mark} | Jump to position of mark | N |
| '' | Jump to previous position | N |
| Ctrl + o | Jump to older position in jump list | N |
| Ctrl + i | Jump to newer position in jump list | N |

## Editing

| Shortcut | Action | Mode |
| --- | --- | --- |
| x | Delete character under cursor | N |
| X | Delete character before cursor | N |
| dw | Delete word | N |
| dd | Delete line | N |
| D | Delete to end of line | N |
| d$ | Delete to end of line | N |
| d0 | Delete to beginning of line | N |
| dgg | Delete to beginning of file | N |
| dG | Delete to end of file | N |
| d{motion} | Delete text covered by motion | N |
| cw | Change word | N |
| cc | Change entire line | N |
| c{motion} | Change text covered by motion | N |
| r{char} | Replace character under cursor | N |
| ~ | Toggle case of character | N |
| g~{motion} | Toggle case of text | N |
| gu{motion} | Make text lowercase | N |
| gU{motion} | Make text uppercase | N |
| >> | Indent line right | N |
| << | Indent line left | N |
| == | Auto-indent line | N |
| ={motion} | Auto-indent text | N |
| J | Join current and next line | N |
| gJ | Join lines without inserting space | N |
| u | Undo | N |
| Ctrl + r | Redo | N |
| . | Repeat last change | N |
| p | Paste after cursor | N |
| P | Paste before cursor | N |
| gp | Paste after cursor, move cursor after paste | N |
| gP | Paste before cursor, move cursor after paste | N |
| y | Yank (copy) | V |
| yy | Yank current line | N |
| Y | Yank to end of line | N |
| y{motion} | Yank text covered by motion | N |

## Search and Replace

| Shortcut | Action | Mode |
| --- | --- | --- |
| /{pattern} | Search forward | N |
| ?{pattern} | Search backward | N |
| n | Next search match | N |
| N | Previous search match | N |
| * | Search for word under cursor (forward) | N |
| # | Search for word under cursor (backward) | N |
| :s/old/new/ | Replace first occurrence on line | C |
| :s/old/new/g | Replace all occurrences on line | C |
| :%s/old/new/g | Replace all occurrences in file | C |
| :%s/old/new/gc | Replace all with confirmation | C |
| :noh | Clear search highlights | C |

## Marks

| Shortcut | Action | Mode |
| --- | --- | --- |
| m{a-z} | Set local mark | N |
| m{A-Z} | Set global mark | N |
| `{mark} | Jump to mark position | N |
| '{mark} | Jump to mark line | N |
| :marks | List all marks | C |

## Registers

| Shortcut | Action | Mode |
| --- | --- | --- |
| "{register}y | Yank into register | N/V |
| "{register}p | Paste from register | N |
| :registers | Show all registers | C |
| Ctrl + r {register} | Paste from register | I |
| "" | Unnamed (default) register | N |
| "0 | Last yank register | N |
| "1–"9 | Numbered registers (last deletes) | N |
| "+ | System clipboard register | N |
| "* | Selection clipboard register | N |
| "_ | Black hole register | N |
| ": | Last command register | N |
| "/ | Last search register | N |

## Windows and Splits

| Shortcut | Action | Mode |
| --- | --- | --- |
| :sp | Split window horizontally | C |
| :vsp | Split window vertically | C |
| :split {file} | Open file in horizontal split | C |
| :vsplit {file} | Open file in vertical split | C |
| Ctrl + w s | Horizontal split | N |
| Ctrl + w v | Vertical split | N |
| Ctrl + w h | Move to left window | N |
| Ctrl + w j | Move to window below | N |
| Ctrl + w k | Move to window above | N |
| Ctrl + w l | Move to right window | N |
| Ctrl + w w | Cycle through windows | N |
| Ctrl + w c | Close current window | N |
| Ctrl + w o | Close all other windows | N |
| Ctrl + w = | Make windows equal size | N |
| Ctrl + w + | Increase window height | N |
| Ctrl + w - | Decrease window height | N |
| Ctrl + w > | Increase window width | N |
| Ctrl + w < | Decrease window width | N |
| Ctrl + w r | Rotate windows | N |
| Ctrl + w H | Move window to far left | N |
| Ctrl + w J | Move window to bottom | N |
| Ctrl + w K | Move window to top | N |
| Ctrl + w L | Move window to far right | N |

## Tabs

| Shortcut | Action | Mode |
| --- | --- | --- |
| :tabnew | Open new tab | C |
| :tabnew {file} | Open file in new tab | C |
| :tabclose | Close current tab | C |
| :tabonly | Close all other tabs | C |
| gt | Next tab | N |
| gT | Previous tab | N |
| {n}gt | Go to tab n | N |
| :tabs | List all tabs | C |

## Buffers

| Shortcut | Action | Mode |
| --- | --- | --- |
| :e {file} | Open file in buffer | C |
| :ls | List all buffers | C |
| :b {n} | Switch to buffer n | C |
| :bp | Previous buffer | C |
| :bn | Next buffer | C |
| :bd | Delete (close) buffer | C |
| :bw | Wipe buffer | C |
| :bufdo {cmd} | Execute command on all buffers | C |
| Ctrl + ^ | Switch to alternate buffer | N |

## File Operations

| Shortcut | Action | Mode |
| --- | --- | --- |
| :w | Save file | C |
| :w {file} | Save as new file | C |
| :wq | Save and quit | C |
| :x | Save and quit (only if modified) | C |
| ZZ | Save and quit | N |
| :q | Quit | C |
| :q! | Quit without saving | C |
| ZQ | Quit without saving | N |
| :qa | Quit all windows | C |
| :wa | Save all buffers | C |
| :wqa | Save all and quit | C |

## Visual Mode

| Shortcut | Action | Mode |
| --- | --- | --- |
| v | Character-wise visual | N |
| V | Line-wise visual | N |
| Ctrl + v | Block-wise visual | N |
| o | Move to other end of selection | V |
| aw | Select around word | V |
| iw | Select inner word | V |
| aW | Select around WORD | V |
| iW | Select inner WORD | V |
| a( / a) / ab | Select around parentheses | V |
| i( / i) / ib | Select inside parentheses | V |
| a[ / a] | Select around brackets | V |
| i[ / i] | Select inside brackets | V |
| a{ / a} / aB | Select around braces | V |
| i{ / i} / iB | Select inside braces | V |
| a" | Select around double quotes | V |
| i" | Select inside double quotes | V |
| a' | Select around single quotes | V |
| i' | Select inside single quotes | V |
| gv | Reselect last visual selection | N |
| > | Indent selection | V |
| < | Unindent selection | V |
| ~ | Toggle case | V |
| u | Make lowercase | V |
| U | Make uppercase | V |

## Macros

| Shortcut | Action | Mode |
| --- | --- | --- |
| q{register} | Start recording macro | N |
| q | Stop recording macro | N |
| @{register} | Play macro | N |
| @@ | Replay last macro | N |
| {n}@{register} | Play macro n times | N |

## Folding

| Shortcut | Action | Mode |
| --- | --- | --- |
| zf{motion} | Create fold | N |
| zd | Delete fold at cursor | N |
| zD | Delete folds recursively | N |
| zo | Open fold at cursor | N |
| zO | Open folds recursively | N |
| zc | Close fold at cursor | N |
| zC | Close folds recursively | N |
| za | Toggle fold at cursor | N |
| zA | Toggle folds recursively | N |
| zr | Reduce folding (open one level) | N |
| zR | Open all folds | N |
| zm | Increase folding (close one level) | N |
| zM | Close all folds | N |
| zn | Disable folding | N |
| zN | Re-enable folding | N |

## Miscellaneous

| Shortcut | Action | Mode |
| --- | --- | --- |
| Ctrl + g | Show file info and cursor position | N |
| ga | Show ASCII value of character | N |
| g8 | Show UTF-8 encoding of character | N |
| :!{cmd} | Execute shell command | C |
| !! | Execute shell command and replace line | N |
| Ctrl + z | Suspend Neovim to shell | N |
| :help {topic} | Open help | C |
| K | Open help for word under cursor | N |
