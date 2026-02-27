# Neovim Quick Reference

> Nvim `:help` pages, generated from source using the tree-sitter-vimdoc parser.
> `N` is used to indicate an optional count that can be given before the command.

## Contents

| Tag | Subject | Tag | Subject |
| --- | --- | --- | --- |
| Q_ct | list of help files | Q_re | Repeating commands |
| Q_lr | motion: Left-right | Q_km | Key mapping |
| Q_ud | motion: Up-down | Q_ab | Abbreviations |
| Q_tm | motion: Text object | Q_op | Options |
| Q_pa | motion: Pattern searches | Q_ur | Undo/Redo commands |
| Q_ma | motion: Marks | Q_et | External commands |
| Q_vm | motion: Various | Q_qf | Quickfix commands |
| Q_ta | motion: Using tags | Q_vc | Various commands |
| Q_sc | Scrolling | Q_ce | Ex: Command-line editing |
| Q_in | insert: Inserting text | Q_ra | Ex: Ranges |
| Q_ai | insert: Keys | Q_ex | Ex: Special characters |
| Q_ss | insert: Special keys | Q_st | Starting Vim |
| Q_di | insert: Digraphs | Q_ed | Editing a file |
| Q_si | insert: Special inserts | Q_fl | Using the argument list |
| Q_de | change: Deleting text | Q_wq | Writing and quitting |
| Q_cm | change: Copying and moving | Q_ac | Automatic commands |
| Q_ch | change: Changing text | Q_wi | Multi-window commands |
| Q_co | change: Complex | Q_bu | Buffer list commands |
| Q_vi | Visual mode | Q_sy | Syntax highlighting |
| Q_to | Text objects | Q_gu | GUI commands |
| Q_fo | Folding | | |

## Q_lr — Left-right motions

| Command | Description |
| --- | --- |
| `N h` | left (also: `CTRL-H`, `BS`, or `Left` key) |
| `N l` | right (also: `Space` or `Right` key) |
| `0` | to first character in the line (also: `Home` key) |
| `^` | to first non-blank character in the line |
| `N $` | to the last character in the line (also: `End` key) |
| `g0` | to first character in screen line (differs from `0` when lines wrap) |
| `g^` | to first non-blank character in screen line |
| `N g$` | to last character in screen line |
| `gm` | to middle of the screen line |
| `N \|` | to column N (default: 1) |
| `N f{char}` | to Nth occurrence of {char} to the right |
| `N F{char}` | to Nth occurrence of {char} to the left |
| `N t{char}` | till before Nth occurrence of {char} to the right |
| `N T{char}` | till before Nth occurrence of {char} to the left |
| `N ;` | repeat the last `f`, `F`, `t`, or `T` N times |
| `N ,` | repeat the last `f`, `F`, `t`, or `T` N times in opposite direction |

## Q_ud — Up-down motions

| Command | Description |
| --- | --- |
| `N k` | up N lines (also: `CTRL-P` and `Up` key) |
| `N j` | down N lines (also: `CTRL-J`, `CTRL-N`, `NL`, and `Down` key) |
| `N -` | up N lines, on the first non-blank character |
| `N +` | down N lines, on the first non-blank character (also: `CTRL-M` and `CR`) |
| `N _` | down N-1 lines, on the first non-blank character |
| `N G` | to line N (default: last line), on the first non-blank character |
| `N gg` | to line N (default: first line), on the first non-blank character |
| `N %` | to line N percentage down in the file; N must be given, otherwise it is the `%` command |
| `N gk` | up N screen lines (differs from `k` when line wraps) |
| `N gj` | down N screen lines (differs from `j` when line wraps) |

## Q_tm — Text object motions

| Command | Description |
| --- | --- |
| `N w` | N words forward |
| `N W` | N blank-separated WORDs forward |
| `N e` | forward to the end of the Nth word |
| `N E` | forward to the end of the Nth blank-separated WORD |
| `N b` | N words backward |
| `N B` | N blank-separated WORDs backward |
| `N ge` | backward to the end of the Nth word |
| `N gE` | backward to the end of the Nth blank-separated WORD |
| `N )` | N sentences forward |
| `N (` | N sentences backward |
| `N }` | N paragraphs forward |
| `N {` | N paragraphs backward |
| `N ]]` | N sections forward, at the start |
| `N [[` | N sections backward, at the start |
| `N ][` | N sections forward, at the end |
| `N []` | N sections backward, at the end |
| `N [(` | N times back to unclosed `(` |
| `N [{` | N times back to unclosed `{` |
| `N [m` | N times back to start of method (for Java) |
| `N [M` | N times back to end of method (for Java) |
| `N ])` | N times forward to unclosed `)` |
| `N ]}` | N times forward to unclosed `}` |
| `N ]m` | N times forward to start of method (for Java) |
| `N ]M` | N times forward to end of method (for Java) |
| `N [#` | N times back to unclosed `#if` or `#else` |
| `N ]#` | N times forward to unclosed `#else` or `#endif` |
| `N [*` | N times back to start of a C comment `/*` |
| `N ]*` | N times forward to end of a C comment `*/` |

## Q_pa — Pattern searches

| Command | Description |
| --- | --- |
| `N /{pattern}[/[offset]]` | search forward for the Nth occurrence of {pattern} |
| `N ?{pattern}[?[offset]]` | search backward for the Nth occurrence of {pattern} |
| `N /` | repeat last search, in the forward direction |
| `N ?` | repeat last search, in the backward direction |
| `N n` | repeat last search in same direction |
| `N N` | repeat last search in opposite direction |
| `N *` | search forward for the identifier under the cursor |
| `N #` | search backward for the identifier under the cursor |
| `N g*` | like `*`, but also find partial matches |
| `N g#` | like `#`, but also find partial matches |
| `gd` | go to local declaration of identifier under the cursor |
| `gD` | go to global declaration of identifier under the cursor |

## Q_ma — Marks and motions

| Command | Description |
| --- | --- |
| `m{a-zA-Z}` | mark current position with mark {a-zA-Z} |
| `` `{a-z} `` | go to mark {a-z} within current file |
| `` `{A-Z} `` | go to mark {A-Z} in any file |
| `` `{0-9} `` | go to the position where Vim was previously exited |
| ` `` ` | go to the position before the last jump |
| `` `" `` | go to the position when last editing this file |
| `` `[ `` | go to the start of the previously operated or put text |
| `` `] `` | go to the end of the previously operated or put text |
| `` `< `` | go to the start of the last visual area |
| `` `> `` | go to the end of the last visual area |
| `` `. `` | go to the position of the last change in this file |
| `'{a-zA-Z0-9[]'"<>.}` | same as `` ` `` moves, but to the first non-blank in the line |
| `:marks` | print the active marks |
| `N CTRL-O` | go to Nth older position in jump list |
| `N CTRL-I` | go to Nth newer position in jump list |
| `:jumps` | print the jump list |
| `N g;` | go to Nth older position in change list |
| `N g,` | go to Nth newer position in change list |
| `:changes` | print the change list |

## Q_vm — Various motions

| Command | Description |
| --- | --- |
| `%` | find the next brace, bracket, comment, or `#if`/`#else`/`#endif` in this line and go to its match |
| `N H` | go to the Nth line in the window, on the first non-blank |
| `M` | go to the middle line in the window, on the first non-blank |
| `N L` | go to the Nth line from the bottom, on the first non-blank |
| `N go` | go to Nth byte in the buffer |
| `:[range]go[to] [off]` | go to [off] byte in the buffer |

## Q_ta — Using tags

| Command | Description |
| --- | --- |
| `:ta[g][!] {tag}` | jump to tag {tag} |
| `:ta[g][!]` | jump to newer tag in tag list |
| `N CTRL-T` | jump back from Nth older tag in tag list |
| `:po[p][!]` | jump back from Nth older tag in tag list |
| `:tags` | print tag list |
| `N CTRL-]` | jump to the definition of the keyword under the cursor |
| `N g]` | like `CTRL-]` but show a list of matching tags |
| `N g CTRL-]` | like `CTRL-]` but show a list of matching tags if there are multiple |
| `:ts[elect][!] [tag]` | list matching tags and select one to jump to |
| `:tj[ump][!] [tag]` | jump to tag or show list of matching tags |
| `:lt[ag][!] [tag]` | jump to tag, add to location list |
| `:ptag {tag}` | open a preview window to show tag {tag} |
| `CTRL-W }` | like `CTRL-]` but show in preview window |
| `:pts[elect] [tag]` | like `:tselect` but show in preview window |
| `:ptj[ump] [tag]` | like `:tjump` but show in preview window |
| `:pc[lose]` | close the preview window |
| `CTRL-W z` | close the preview window |

## Q_sc — Scrolling

| Command | Description |
| --- | --- |
| `N CTRL-E` | window N lines downward (default: 1) |
| `N CTRL-D` | window N lines downward (default: 1/2 window) |
| `N CTRL-F` | window N pages downward (forward) |
| `N CTRL-Y` | window N lines upward (default: 1) |
| `N CTRL-U` | window N lines upward (default: 1/2 window) |
| `N CTRL-B` | window N pages upward (backward) |
| `z CR` or `zt` | redraw, cursor line to top of window |
| `z.` or `zz` | redraw, cursor line to center of window |
| `z-` or `zb` | redraw, cursor line to bottom of window |
| `N zh` | scroll screen N characters to the right |
| `N zl` | scroll screen N characters to the left |
| `N zH` | scroll screen half a screenwidth to the right |
| `N zL` | scroll screen half a screenwidth to the left |

## Q_in — Inserting text

| Command | Description |
| --- | --- |
| `N a` | append text after the cursor (N times) |
| `N A` | append text at the end of the line (N times) |
| `N i` | insert text before the cursor (N times) |
| `N I` | insert text before the first non-blank in the line (N times) |
| `N gI` | insert text in column 1 (N times) |
| `gi` | insert text at the end of the last insert |
| `N o` | open a new line below the current line, append text (N times) |
| `N O` | open a new line above the current line, append text (N times) |

## Q_ai — Insert mode keys

| Command | Description |
| --- | --- |
| `CTRL-[`, `ESC` | end insert mode, back to Normal mode |
| `CTRL-C` | quit insert mode without a character inserted |
| `CTRL-@` | insert previously inserted text and stop insert |
| `CTRL-A` | insert previously inserted text |
| `CTRL-R {reg}` | insert the contents of a register |
| `CTRL-R CTRL-R {reg}` | insert the contents of a register literally |
| `CTRL-\` `CTRL-O {cmd}` | execute Vim command {cmd} without moving the cursor |
| `CTRL-O {cmd}` | execute Vim command {cmd} |
| `CTRL-N` | complete Next keyword |
| `CTRL-P` | complete Previous keyword |
| `CTRL-X` | complete using specific methods |
| `CTRL-E` | scroll screen one line up |
| `CTRL-Y` | scroll screen one line down |
| `CTRL-T` | insert one `shiftwidth` of indent |
| `CTRL-D` | delete one `shiftwidth` of indent |
| `0 CTRL-D` | delete all indent in current line |
| `CTRL-V {char}` | insert next non-digit literally |
| `CTRL-V {dec}` | enter decimal value of character |
| `CTRL-V o{oct}` | enter octal value of character |
| `CTRL-V x{hex}` | enter hexadecimal value of character |
| `CTRL-K {k1}{k2}` | enter digraph |
| `CTRL-_` | switch between languages (only with `allowrevins` set) |

## Q_ss — Insert mode special keys

| Command | Description |
| --- | --- |
| `BS` | delete character before the cursor |
| `Del` | delete character under the cursor |
| `CTRL-W` | delete word before the cursor |
| `CTRL-U` | delete all entered characters in the current line |
| `CTRL-H` | same as `BS` |
| `Left` | cursor one character left |
| `Shift-Left` | cursor one word left |
| `Right` | cursor one character right |
| `Shift-Right` | cursor one word right |
| `Up` | cursor one line up |
| `Down` | cursor one line down |
| `End` | cursor after last character in the line |
| `Home` | cursor to first character in the line |
| `PageUp` | one screenful backward |
| `PageDown` | one screenful forward |
| `CTRL-\` `CTRL-N` | go to Normal mode |
| `CTRL-\` `CTRL-G` | go to Normal mode |

## Q_di — Digraphs

| Command | Description |
| --- | --- |
| `:dig[raphs]` | show current list of digraphs |
| `:dig[raphs] {chars1}{char} ...` | add digraphs to the list |

## Q_si — Special inserts

| Command | Description |
| --- | --- |
| `:r [file]` | insert the contents of [file] below the cursor line |
| `:r! {cmd}` | insert the standard output of {cmd} below the cursor line |

## Q_de — Deleting text

| Command | Description |
| --- | --- |
| `N x` | delete N characters under and after the cursor |
| `N X` | delete N characters before the cursor |
| `N dd` | delete N lines |
| `N D` | delete to the end of the line (and N-1 more lines) |
| `N d{motion}` | delete the text that is moved over with {motion} |
| `{visual}d` | delete the highlighted text |
| `N J` | join N-1 lines (delete EOLs) |
| `{visual}J` | join the highlighted lines |
| `N gJ` | like `J`, but without inserting spaces |
| `{visual}gJ` | like `{visual}J`, but without inserting spaces |
| `:[range]d [x]` | delete [range] lines [into register x] |

## Q_cm — Copying and moving text

| Command | Description |
| --- | --- |
| `"{char}` | use register {char} for the next delete, yank, or put |
| `"*` | use the clipboard register for the next delete, yank, or put |
| `:reg` | show the contents of all registers |
| `:reg {arg}` | show the contents of registers matching {arg} |
| `N yy` | yank N lines into a register (also: `Y`) |
| `N y{motion}` | yank the text moved over with {motion} into a register |
| `{visual}y` | yank the highlighted text into a register |
| `N p` | put a register after the cursor position (N times) |
| `N P` | put a register before the cursor position (N times) |
| `N ]p` | like `p`, but adjust indent to current line |
| `N [p` | like `P`, but adjust indent to current line |
| `N gp` | like `p`, but leave cursor after the new text |
| `N gP` | like `P`, but leave cursor after the new text |

## Q_ch — Changing text

| Command | Description |
| --- | --- |
| `N r{char}` | replace N characters with {char} |
| `N R` | enter Replace mode (repeat the entered text N times) |
| `N gr{char}` | replace N characters without affecting layout (virtual replace) |
| `N gR` | enter Virtual Replace mode |
| `{visual}r{char}` | in Visual block, virtual, or regular mode: replace each char with {char} |
| `N s` | (substitute) delete N characters and start insert (same as `cl`) |
| `N S` | delete N lines and start insert (same as `cc`) |
| `N c{motion}` | delete the text that motion moves over and start insert |
| `N cc` | delete N lines and start insert |
| `N C` | delete to end of line and start insert (same as `c$`) |
| `N ~` | switch case for N characters and advance cursor |
| `{visual}~` | switch case for highlighted text |
| `{visual}u` | make highlighted text lowercase |
| `{visual}U` | make highlighted text uppercase |
| `g~{motion}` | switch case for the text that is moved over |
| `gu{motion}` | make the text that is moved over lowercase |
| `gU{motion}` | make the text that is moved over uppercase |
| `{visual}g?` | perform rot13 encoding on the highlighted text |
| `g?{motion}` | perform rot13 encoding on the text that is moved over |
| `N CTRL-A` | add N to the number at or after the cursor |
| `N CTRL-X` | subtract N from the number at or after the cursor |
| `N <{motion}` | move the lines that are moved over one `shiftwidth` left |
| `N <<` | move N lines one `shiftwidth` left |
| `N >{motion}` | move the lines that are moved over one `shiftwidth` right |
| `N >>` | move N lines one `shiftwidth` right |
| `N gq{motion}` | format the lines that are moved over |
| `N gqq` | format N lines |
| `:{range}ce[nter] [width]` | center the lines in [range] |
| `:{range}le[ft] [indent]` | left-align the lines in [range] (with [indent]) |
| `:{range}ri[ght] [width]` | right-align the lines in [range] |

## Q_co — Complex changes

| Command | Description |
| --- | --- |
| `N !{motion}{cmd}` | filter the lines that are moved over through {cmd} |
| `N !!{cmd}` | filter N lines through {cmd} |
| `{visual}!{cmd}` | filter the highlighted lines through {cmd} |
| `:{range}! {cmd}` | filter [range] lines through {cmd} |
| `N ={motion}` | filter the lines that are moved over through `equalprg` |
| `N ==` | filter N lines through `equalprg` |
| `{visual}=` | filter the highlighted lines through `equalprg` |
| `:[range]s[ubstitute]/{pat}/{str}/[g][c]` | substitute {pat} with {str} in [range] lines; with `g`, replace all occurrences of {pat}; with `c`, confirm each replacement |
| `:[range]s[ubstitute] [g][c]` | repeat last `:s` with new range and/or flags |
| `&` | repeat last `:s` on current line without flags |
| `:[range]ret[ab][!] [tabstop]` | set `tabstop` and retabulate the lines |

## Q_vi — Visual mode

| Command | Description |
| --- | --- |
| `v` | start characterwise visual mode |
| `V` | start linewise visual mode |
| `CTRL-V` | start blockwise visual mode |
| `o` | exchange cursor position with start of the highlighted area |
| `gv` | start Visual mode with the previous highlighted area |
| `v_o` | move cursor to other corner of area |
| `v_$` | when in Visual block mode, extend till the last character of the line |
| `{visual}d` | delete the highlighted area |
| `{visual}D` | when in Visual block mode, delete till the end of the line |
| `{visual}c` | delete the highlighted area and start insert |
| `{visual}C` | when in Visual block mode, delete till the end of the line and start insert |
| `{visual}y` | yank the highlighted area |
| `{visual}Y` | when in Visual block mode, yank till the end of the line |
| `{visual}>` | shift the highlighted lines one `shiftwidth` right |
| `{visual}<` | shift the highlighted lines one `shiftwidth` left |

## Q_to — Text objects (only in Visual mode or after an operator)

| Command | Description |
| --- | --- |
| `N aw` | "a word" (with white space) |
| `N iw` | "inner word" (without white space) |
| `N aW` | "a WORD" (with white space) |
| `N iW` | "inner WORD" (without white space) |
| `N as` | "a sentence" (with white space) |
| `N is` | "inner sentence" (without white space) |
| `N ap` | "a paragraph" (with white space) |
| `N ip` | "inner paragraph" (without white space) |
| `N ab` | "a block" from `[` to `]` (with braces) |
| `N ib` | "inner block" from `[` to `]` |
| `N aB` | "a Block" from `{` to `}` (with braces) |
| `N iB` | "inner Block" from `{` to `}` |
| `N at` | "a tag block" (with tags) |
| `N it` | "inner tag block" (without tags) |
| `N a<` | "a `<>` block" (with angle brackets) |
| `N i<` | "inner `<>` block" |
| `N a[` | "a `[]` block" (with brackets) |
| `N i[` | "inner `[]` block" |
| `N a(` or `N a)` | "a block" from `(` to `)` |
| `N i(` or `N i)` | "inner block" from `(` to `)` |
| `N a{` or `N a}` | "a Block" from `{` to `}` |
| `N i{` or `N i}` | "inner Block" from `{` to `}` |
| `N a"` | double quoted string (with quotes) |
| `N i"` | double quoted string (without quotes) |
| `N a'` | single quoted string (with quotes) |
| `N i'` | single quoted string (without quotes) |
| `` N a` `` | string in backticks (with backticks) |
| `` N i` `` | string in backticks (without backticks) |

## Q_re — Repeating commands

| Command | Description |
| --- | --- |
| `N .` | repeat last change (with count replaced by N) |
| `q{a-z}` | record typed characters into register {a-z} |
| `q{A-Z}` | record typed characters, appended to register {a-z} |
| `q` | stop recording |
| `N @{a-z}` | execute the contents of register {a-z} (N times) |
| `N @@` | repeat previous `@{a-z}` (N times) |
| `:@{a-z}` | execute the contents of register {a-z} as an Ex command |
| `:@@` | repeat previous `:@{a-z}` |
| `:[range]g[lobal]/{pat}/[cmd]` | execute Ex command [cmd] (default: `:p`) on the lines within [range] where {pat} matches |
| `:[range]g[lobal]!/{pat}/[cmd]` | execute Ex command [cmd] (default: `:p`) on the lines within [range] where {pat} does NOT match |
| `:so[urce] {file}` | read Ex commands from {file} |
| `:so[urce]! {file}` | read Vim commands from {file} |
| `:sl[eep] [sec]` | don't do anything for [sec] seconds |
| `N gs` | go to sleep for N seconds |

## Q_km — Key mapping

| Command | Description |
| --- | --- |
| `:ma[p] {lhs} {rhs}` | map {lhs} to {rhs} in Normal and Visual mode |
| `:ma[p]! {lhs} {rhs}` | map {lhs} to {rhs} in Insert and Command-line mode |
| `:nm[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Normal mode |
| `:vm[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Visual mode |
| `:om[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Operator-pending mode |
| `:im[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Insert mode |
| `:lm[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Insert, Command-line, and Lang-Arg mode |
| `:cm[ap] {lhs} {rhs}` | map {lhs} to {rhs} in Command-line mode |
| `:no[remap] {lhs} {rhs}` | same as `:map`, but not remappable |
| `:nn[oremap] {lhs} {rhs}` | same as `:nmap`, but not remappable |
| `:vn[oremap] {lhs} {rhs}` | same as `:vmap`, but not remappable |
| `:ono[remap] {lhs} {rhs}` | same as `:omap`, but not remappable |
| `:ino[remap] {lhs} {rhs}` | same as `:imap`, but not remappable |
| `:ln[oremap] {lhs} {rhs}` | same as `:lmap`, but not remappable |
| `:cno[remap] {lhs} {rhs}` | same as `:cmap`, but not remappable |
| `:unm[ap] {lhs}` | remove the mapping of {lhs} for Normal and Visual mode |
| `:unm[ap]! {lhs}` | remove the mapping of {lhs} for Insert and Command-line mode |
| `:nun[map] {lhs}` | remove the mapping of {lhs} for Normal mode |
| `:vun[map] {lhs}` | remove the mapping of {lhs} for Visual mode |
| `:oun[map] {lhs}` | remove the mapping of {lhs} for Operator-pending mode |
| `:iun[map] {lhs}` | remove the mapping of {lhs} for Insert mode |
| `:lun[map] {lhs}` | remove the mapping of {lhs} for Lang-Arg mode |
| `:cun[map] {lhs}` | remove the mapping of {lhs} for Command-line mode |
| `:ma[p]` | list all key mappings for Normal and Visual mode |
| `:ma[p]!` | list all key mappings for Insert and Command-line mode |
| `:nm[ap]` | list all key mappings for Normal mode |
| `:vm[ap]` | list all key mappings for Visual mode |
| `:om[ap]` | list all key mappings for Operator-pending mode |
| `:im[ap]` | list all key mappings for Insert mode |
| `:lm[ap]` | list all key mappings for Lang-Arg mode |
| `:cm[ap]` | list all key mappings for Command-line mode |

## Q_ab — Abbreviations

| Command | Description |
| --- | --- |
| `:ab[breviate] {lhs} {rhs}` | add abbreviation for {lhs} to {rhs} in Insert mode |
| `:ab[breviate]` | list all abbreviations |
| `:una[bbreviate] {lhs}` | remove abbreviation for {lhs} |
| `:cab[breviate] {lhs} {rhs}` | add abbreviation for {lhs} to {rhs} in Command-line mode |
| `:cuna[bbreviate] {lhs}` | remove abbreviation for {lhs} in Command-line mode |
| `:iab[breviate] {lhs} {rhs}` | add abbreviation for {lhs} to {rhs} in Insert mode only |
| `:iuna[bbreviate] {lhs}` | remove abbreviation for {lhs} in Insert mode only |

## Q_op — Options

| Command | Description |
| --- | --- |
| `:se[t]` | show all modified options |
| `:se[t] all` | show all options |
| `:se[t] {option}` | set boolean option (switch it on) |
| `:se[t] no{option}` | reset boolean option (switch it off) |
| `:se[t] inv{option}` | invert boolean option |
| `:se[t] {option}={value}` | set string/number option to {value} |
| `:se[t] {option}+={value}` | append {value} to string option, add {value} to number option |
| `:se[t] {option}-={value}` | remove {value} from string option, subtract {value} from number option |
| `:se[t] {option}?` | show value of {option} |
| `:se[t] {option}&` | reset {option} to its default value |
| `:setl[ocal]` | like `:set` but set the local value for options that have one |
| `:setg[lobal]` | like `:set` but set the global value of a local option |
| `:fix[del]` | set value of `t_kD` according to value of `t_kb` |
| `:opt[ions]` | open the Options window |

## Q_ur — Undo/Redo commands

| Command | Description |
| --- | --- |
| `N u` | undo last N changes |
| `N CTRL-R` | redo last N undone changes |
| `U` | restore last changed line |
| `:earlier {N}` | go to older text state (N times) |
| `:earlier {N}s` | go to older text state (N seconds) |
| `:earlier {N}m` | go to older text state (N minutes) |
| `:earlier {N}h` | go to older text state (N hours) |
| `:earlier {N}d` | go to older text state (N days) |
| `:later {N}` | go to newer text state (N times) |
| `:later {N}s` | go to newer text state (N seconds) |
| `:later {N}m` | go to newer text state (N minutes) |
| `:later {N}h` | go to newer text state (N hours) |
| `:later {N}d` | go to newer text state (N days) |

## Q_et — External commands

| Command | Description |
| --- | --- |
| `:sh[ell]` | start a shell |
| `:!{cmd}` | execute {cmd} with a shell |
| `N !!{cmd}` | execute {cmd} with a shell and insert stdout below cursor |
| `N !{motion}{cmd}` | filter the text moved over with {motion} through {cmd} |
| `:{range}![!]{cmd}` | filter [range] lines through {cmd} |
| `:r[ead]! {cmd}` | read stdin from output of {cmd} |
| `:w[rite]! {cmd}` | write [range] lines to stdin of {cmd} |
| `:[range]w[rite] !{cmd}` | write [range] lines to stdin of {cmd} |
| `CTRL-Z` | suspend Vim |

## Q_qf — Quickfix commands

| Command | Description |
| --- | --- |
| `:cc [nr]` | display error [nr] (default: same error) |
| `:cn[ext]` | display the next error |
| `:cN[ext]`, `:cp[revious]` | display the previous error |
| `:cnf[ile]` | display the first error in the next file |
| `:cNf[ile]`, `:cpf[ile]` | display the last error in the previous file |
| `:cr[ewind]` | display the first error |
| `:cla[st]` | display the last error |
| `:cq[uit]` | quit without writing |
| `:cf[ile] [errorfile]` | read errors from [errorfile] |
| `:cg[etfile] [errorfile]` | like `:cfile` but don't jump to the first error |
| `:caddf[ile] [errorfile]` | like `:cfile` but add to the current quickfix list |
| `:cl[ist]` | list all errors |
| `:chi[story]` | list the error lists |
| `:col[der] [nr]` | go to [nr] older error list |
| `:cnew[er] [nr]` | go to [nr] newer error list |
| `:copen [height]` | open the quickfix window |
| `:cw[indow] [height]` | open the quickfix window if there are errors |
| `:ccl[ose]` | close the quickfix window |
| `:vimgrep[add] {pat} {files}` | search for {pat} in {files} |
| `:lv[imgrepadd] {pat} {files}` | like `:vimgrep` but use location list |
| `:gr[ep][add] {pat} {files}` | search for {pat} in {files} using `grepprg` |
| `:lgr[ep][add] {pat} {files}` | like `:grep` but use location list |
| `[N ]q` | go to [N]th previous quickfix entry |
| `[N ]Q` | go to [N]th next quickfix entry |

## Q_vc — Various commands

| Command | Description |
| --- | --- |
| `CTRL-L` | clear and redraw the screen |
| `CTRL-G` | show current file name and cursor position |
| `g CTRL-G` | show cursor position in various formats |
| `N ga` | show ASCII value of character under the cursor |
| `g8` | show UTF-8 bytes for character under the cursor |
| `N gf` | start editing the file whose name is under the cursor |
| `N gF` | like `gf`, but position cursor at line number after the filename |
| `N K` | lookup keyword under the cursor with `keywordprg` |
| `N :K` | lookup keyword under the cursor with `keywordprg` |
| `:p[rint] [N]` | print current file name and number of lines |
| `ZZ` | write if modified then quit |
| `ZQ` | quit without writing |

## Q_ce — Ex: Command-line editing

| Command | Description |
| --- | --- |
| `CTRL-A` | complete all matching command names |
| `CTRL-D` | list all matching command names |
| `Tab` | do completion on the command-line |
| `CTRL-N` | go to next match, when multiple completions exist |
| `CTRL-P` | go to previous match, when multiple completions exist |
| `CTRL-B` | cursor to beginning of command-line |
| `CTRL-E` | cursor to end of command-line |
| `CTRL-H` | delete the character before the cursor |
| `BS` | delete the character before the cursor |
| `CTRL-W` | delete word before the cursor |
| `CTRL-U` | delete all characters before the cursor |
| `CTRL-K {k1}{k2}` | enter digraph |
| `CTRL-R {reg}` | insert the contents of a register |
| `CTRL-R CTRL-W` | insert the word under the cursor |
| `CTRL-R CTRL-A` | insert the WORD under the cursor |
| `CTRL-R CTRL-L` | insert the line under the cursor |
| `CTRL-R CTRL-R {reg}` | insert the contents of a register literally |
| `CTRL-[`, `ESC` | abandon command-line without executing |
| `CTRL-C` | abandon command-line without executing |
| `Up` | recall previous command-line from history (that matches pattern so far) |
| `Down` | recall next command-line from history |
| `CTRL-P` | recall previous command-line from history |
| `CTRL-N` | recall next command-line from history |
| `q:` | open command-line window (Normal mode) |
| `q/` | open command-line window for searches (Normal mode) |
| `q?` | open command-line window for backward searches (Normal mode) |
| `CTRL-F` | switch from command-line to the command-line window |

## Q_ra — Ex: Ranges

| Command | Description |
| --- | --- |
| `,` | separates two line numbers |
| `;` | idem, set cursor to the first line number before interpreting the second |
| `{number}` | an absolute line number |
| `.` | the current line |
| `$` | the last line in the file |
| `%` | equal to `1,$` (the entire file) |
| `*` | equal to `'<,'>` (visual area) |
| `'t` | position of mark t |
| `/{pattern}[/]` | the next line where {pattern} matches |
| `?{pattern}[?]` | the previous line where {pattern} matches |
| `+[num]` | add [num] to the preceding line number (default: 1) |
| `-[num]` | subtract [num] from the preceding line number (default: 1) |

## Q_ex — Ex: Special characters

| Command | Description |
| --- | --- |
| `<CR>` | executes the command |
| `<BS>` | deletes the preceding character |
| `<Esc>` | abandons the command |
| `<C-V>{char}` | inserts {char} literally |
| `<C-V>{dec}` | inserts character with decimal value {dec} |
| `<C-V>o{oct}` | inserts character with octal value {oct} |
| `<C-V>x{hex}` | inserts character with hexadecimal value {hex} |
| `<C-K>{k1}{k2}` | inserts digraph |
| `<Insert>` | toggle insert/overstrike mode |
| `<Up>` | recall previous command from history |
| `<Down>` | recall next command from history |
| `<S-Up>`, `<PageUp>` | recall previous command from history |
| `<S-Down>`, `<PageDown>` | recall next command from history |
| `<Home>` | go to the beginning of the command line |
| `<End>` | go to the end of the command line |
| `<Left>` | cursor left |
| `<Right>` | cursor right |
| `<S-Left>`, `<C-Left>` | cursor one word left |
| `<S-Right>`, `<C-Right>` | cursor one word right |
| `<C-B>` | cursor to beginning of command line |
| `<C-E>` | cursor to end of command line |
| `<C-D>` | list matching completions |
| `<Tab>` | do completion on the command line |
| `<C-N>` | go to next match |
| `<C-P>` | go to previous match |
| `<C-A>` | complete all matching names |
| `<C-L>` | complete name up to a common string |
| `<C-]>` | trigger abbreviation |
| `<C-R>{reg}` | insert register |
| `<C-\>e {expr}` | replace command line with result of {expr} |

## Q_st — Starting Vim

| Command | Description |
| --- | --- |
| `vim [options] [file ..]` | start editing one or more files |
| `vim [options] -` | read file from stdin |
| `vim [options] -t {tag}` | edit file associated with {tag} |
| `vim [options] -q [fname]` | start editing with first error in [fname] |
| `nvim --version` | print version information |
| `nvim --help` | print help message |
| `+[num]` | for the first file: go to line [num] |
| `+/{pat}` | for the first file: go to line with {pat} |
| `+{cmd}`, `-c {cmd}` | execute {cmd} after loading the first file |
| `-S {file}` | source file {file} after loading the first file |
| `--cmd {cmd}` | execute {cmd} before loading any vimrc file |
| `-b` | binary mode |
| `-d` | diff mode (`nvim -d`) |
| `-e` | Ex mode, see `Ex-mode` |
| `-E` | improved Ex mode, see `gQ` |
| `-n` | no swap file, use memory only |
| `-r` | list swap files and exit |
| `-r {file}` | recover crashed session |
| `-R` | read-only mode, implies `-n` |
| `-m` | modifications not allowed (resets `write` option) |
| `-M` | modifications and writing not allowed |
| `-o [N]` | open N windows for each file |
| `-O [N]` | like `-o` but split vertically |
| `-p [N]` | open N tab pages for each file |
| `-u {vimrc}` | use {vimrc} instead of any `.vimrc` |
| `--noplugin` | don't load plugin scripts |
| `-A` | Arabic mode |
| `-H` | Hebrew mode |
| `-F` | Farsi mode |
| `-T {terminal}` | set terminal type to {terminal} |
| `--not-a-term` | skip warning for output not being a terminal |
| `-x` | edit encrypted files |
| `-X` | don't connect to X server |
| `-Z` | restricted mode: shell commands not allowed |
| `-s {scriptin}` | read script file {scriptin} |
| `-w {N}` | set window height to N (for xterm) |
| `-w {scriptout}` | append all typed commands to file {scriptout} |
| `-W {scriptout}` | like `-w` but overwrite the file |

## Q_ed — Editing a file

| Command | Description |
| --- | --- |
| `:e[dit] [++opt] [+cmd] {file}` | edit {file} |
| `:e[dit] [++opt] [+cmd]` | reload the current file |
| `:fin[d] [++opt] [+cmd] {file}` | find {file} in `path` and edit it |
| `CTRL-^` | edit alternate file (also: `:e #`) |
| `N CTRL-^` | edit Nth file in the argument list (also: `:e #N`) |
| `gf` | edit the file whose name is under the cursor |
| `:[range]r[ead] [++opt] [name]` | insert the file [name] below the specified line |
| `:[range]r[ead] [++opt] !{cmd}` | insert the output of {cmd} below the specified line |

## Q_fl — Using the argument list

| Command | Description |
| --- | --- |
| `:ar[gs]` | print the argument list, with the current file in brackets |
| `:ar[gs] [++opt] [+cmd] {arglist}` | define a new argument list |
| `:ar[gs] [++opt] [+cmd]` | reload the argument list |
| `:n[ext] [++opt] [+cmd] [arglist]` | edit the next file; if [arglist] given, use as new argument list |
| `N :n[ext] [++opt] [+cmd]` | edit the Nth next file |
| `:N[ext] [++opt] [+cmd]` | edit the previous file |
| `:fir[st] [++opt] [+cmd]` | edit the first file |
| `:la[st] [++opt] [+cmd]` | edit the last file |
| `N :wn[ext] [++opt] [+cmd]` | write file and edit the Nth next file |
| `:wN[ext] [++opt] [+cmd]` | write file and edit the previous file |
| `:wfir[st] [++opt] [+cmd]` | write file and edit the first file |
| `:wla[st] [++opt] [+cmd]` | write file and edit the last file |
| `:argd[elete] {pat}` | delete files matching {pat} from the argument list |
| `:argd[elete] [N]` | delete the current or [N]th file from the argument list |
| `:arga[dd] [name]` | add [name] or current file to the argument list |

## Q_wq — Writing and quitting

| Command | Description |
| --- | --- |
| `:w[rite] [++opt]` | write to the current file name |
| `:w[rite] [++opt] {file}` | write to {file}, unless it already exists |
| `:w[rite]! [++opt] {file}` | write to {file} |
| `:[range]w[rite][!] [++opt]` | write [range] lines to the current file |
| `:up[date] [++opt]` | like `:write`, but only when the buffer has been modified |
| `:sav[eas] [++opt][!] {file}` | save the file as {file} and use {file} as the current file name |
| `:q[uit]` | quit the current window (when not the last window) |
| `:q[uit]!` | quit without writing, also when the last write failed |
| `:wq [++opt]` | write the current file and quit |
| `:wq! [++opt]` | write the current file and quit, even if file is read-only |
| `:wqa[ll]!` | write all modified files and quit |
| `:x[it]! [++opt]` | like `:wq`, but only write when the file was modified |
| `:xa[ll]` | like `:xall`, but write when modified |
| `ZZ` | write if modified and close window |
| `ZQ` | close window without writing |
| `:qa[ll]` | close all windows, quit Vim |
| `:qa[ll]!` | close all windows, quit Vim without writing |
| `:cq[uit]` | quit without writing and return error code |
| `:wall[!]` | write all changed buffers |

## Q_ac — Automatic commands

| Command | Description |
| --- | --- |
| `:au[tocmd] [group] {event} {pat} [nested] {cmd}` | add {cmd} to the list of commands that Vim will execute on {event} for a file matching {pat} |
| `:au[tocmd] [group] {event} {pat}` | show the autocommands for {event} and {pat} |
| `:au[tocmd] [group] * {pat}` | show the autocommands for {pat} |
| `:au[tocmd] [group] {event}` | show the autocommands for {event} |
| `:au[tocmd] [group]` | show all autocommands |
| `:au[tocmd]! [group] {event} {pat} [nested] {cmd}` | remove all autocommands for {event} and {pat}, then add {cmd} |
| `:au[tocmd]! [group] {event} {pat}` | remove all autocommands for {event} and {pat} |
| `:au[tocmd]! [group] * {pat}` | remove all autocommands for {pat} |
| `:au[tocmd]! [group] {event}` | remove all autocommands for {event} |
| `:au[tocmd]! [group]` | remove all autocommands |
| `:aug[roup] {name}` | define the autocmd group name for the following `:au` commands |
| `:aug[roup]! {name}` | delete the autocmd group {name} |

## Q_wi — Multi-window commands

| Command | Description |
| --- | --- |
| `CTRL-W s`, `:sp[lit]` | split current window into two horizontal windows |
| `CTRL-W v`, `:vs[plit]` | split current window into two vertical windows |
| `CTRL-W n`, `:new` | create a new empty window |
| `:new {file}` | edit {file} in a new window |
| `:sv[iew] {file}` | like `:split` but set `readonly` |
| `:sf[ind] {file}` | like `:split` but search for {file} in `path` |
| `CTRL-W ]` | split window and jump to tag under cursor |
| `CTRL-W f` | split window and edit file name under cursor |
| `CTRL-W ^` | split window and edit alternate file |
| `CTRL-W i` | split window and jump to tag declaration of word under cursor |
| `CTRL-W d` | split window and jump to definition under cursor |
| `CTRL-W CTRL-W` | move cursor to the next window (wrap around) |
| `CTRL-W W` | move cursor to the previous window |
| `CTRL-W t` | move cursor to the top-left window |
| `CTRL-W b` | move cursor to the bottom-right window |
| `CTRL-W p` | move cursor to previous (last accessed) window |
| `CTRL-W P` | move cursor to preview window |
| `N CTRL-W _` | set current window height to N (default: very high) |
| `N CTRL-W \|` | set current window width to N (default: very wide) |
| `N CTRL-W +` | increase window height by N |
| `N CTRL-W -` | decrease window height by N |
| `N CTRL-W <` | decrease window width by N |
| `N CTRL-W >` | increase window width by N |
| `CTRL-W =` | make all windows the same height and width |
| `N CTRL-W H` | move current window to far left |
| `N CTRL-W J` | move current window to the very bottom |
| `N CTRL-W K` | move current window to the very top |
| `N CTRL-W L` | move current window to far right |
| `N CTRL-W r` | rotate windows downward |
| `N CTRL-W R` | rotate windows upward |
| `N CTRL-W x` | exchange current window with the Nth window |
| `CTRL-W T` | move current window to a new tab page |
| `CTRL-W z` | close preview window |
| `:pc[lose]` | close preview window |
| `:on[ly]` | close all but the current window |
| `CTRL-W o` | close all but the current window |
| `:q[uit]` | quit current window (when more than one window) |

## Q_bu — Buffer list commands

| Command | Description |
| --- | --- |
| `:ls` or `:files` | list all known buffer and file names |
| `:buffers` | list all known buffer and file names |
| `:b[uffer] [N]` | edit buffer [N] from the buffer list |
| `:b[uffer] {bufname}` | edit buffer for {bufname} from the buffer list |
| `:sb[uffer] [N]` | split window and edit buffer [N] |
| `:bm[odified] [N]` | go to Nth modified buffer |
| `:sbm[odified] [N]` | split window and go to Nth modified buffer |
| `:bn[ext] [N]` | go to Nth next buffer in the buffer list |
| `:sbn[ext] [N]` | split window and go to Nth next buffer |
| `:bN[ext] [N]`, `:bp[revious] [N]` | go to Nth previous buffer in the buffer list |
| `:sbN[ext] [N]`, `:sbp[revious] [N]` | split window and go to Nth previous buffer |
| `:br[ewind]` | go to first buffer in the buffer list |
| `:sbr[ewind]` | split window and go to first buffer in the list |
| `:bl[ast]` | go to last buffer in the buffer list |
| `:sbl[ast]` | split window and go to last buffer in the list |
| `:unh[ide] [N]` | open a window for each buffer in the list |
| `:ba[ll] [N]` | open a window for each buffer in the list |
| `:bad[d] {fname}` | add {fname} to buffer list |
| `:bd[elete][!] [N]` | unload buffer [N] and delete it from the buffer list |
| `:bw[ipeout][!] [N]` | like `:bdelete` but free the memory |
| `CTRL-^` | edit the alternate file (equivalent to `:e #`) |

## Q_sy — Syntax highlighting

| Command | Description |
| --- | --- |
| `:syn[tax] enable` | enable syntax highlighting |
| `:syn[tax] on` | enable syntax highlighting, overrule color settings |
| `:syn[tax] off` | disable syntax highlighting |
| `:syn[tax] reset` | reset syntax highlighting |
| `:syn[tax] clear` | clear all syntax patterns |
| `:syn[tax] list` | list current syntax items |
| `:syn[tax] manual` | enable syntax highlighting, must use `:syntax on` to enable |
| `:set ft=c` | set filetype to C (triggers syntax highlighting) |
| `:set syntax=cpp` | set syntax highlighting to C++ |
| `:colorscheme {name}` | load a colorscheme |
| `:colorscheme` | show current colorscheme |
| `:hi[ghlight] [group] [key=val]` | set highlighting for {group} |
| `:hi[ghlight]` | show all highlighting groups |

## Q_fo — Folding

| Command | Description |
| --- | --- |
| `zf{motion}` | create a fold for the lines moved over |
| `:{range}fo[ld]` | create a fold for [range] lines |
| `zd` | delete one fold at the cursor |
| `zD` | delete all folds at the cursor (recursively) |
| `zE` | eliminate all folds in the window |
| `zo` | open one fold at the cursor |
| `zO` | open all folds at the cursor recursively |
| `zc` | close one fold at the cursor |
| `zC` | close all folds at the cursor recursively |
| `za` | toggle one fold at the cursor |
| `zA` | toggle all folds at the cursor recursively |
| `zv` | view cursor line: open just enough folds |
| `zx` | update folds: undo manually opened/closed folds |
| `zX` | undo manually opened and closed folds |
| `zm` | fold more: increase `foldlevel` by one |
| `zM` | close all folds: set `foldlevel` to 0 |
| `zr` | reduce folding: decrease `foldlevel` by one |
| `zR` | open all folds: set `foldlevel` to maximum |
| `zn` | fold none: reset `foldenable` |
| `zN` | fold normal: set `foldenable` |
| `zi` | invert `foldenable` |
| `[z` | move to the start of the current open fold |
| `]z` | move to the end of the current open fold |
| `zk` | move to the end of the previous fold |
| `zj` | move to the start of the next fold |
| `:foldopen[!]` | open folds in the current line; with `!` all folds |
| `:foldclose[!]` | close folds in the current line; with `!` all folds |
| `:folddoopen {cmd}` | execute {cmd} on all lines not in a closed fold |
| `:folddoclosed {cmd}` | execute {cmd} on all lines in a closed fold |

## Q_gu — GUI commands

| Command | Description |
| --- | --- |
| `:gui` | start the GUI (only when compiled in) |
| `:gvim` | start the GUI |
| `:set guifont={font}` | set the font to use |
| `:set guioptions+={flag}` | add flag to the GUI options |
| `:set guioptions-={flag}` | remove flag from the GUI options |
| `CTRL-Y` | scroll window one line up |
| `CTRL-E` | scroll window one line down |
| `<MiddleMouse>` | paste |
| `<RightMouse>` | popup menu |
