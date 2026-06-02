---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/IDEsAndTextEditorPlugins"
source_path: "sources/raw/external/go-dev-wiki-idesandtexteditorplugins-c7a534c392.html"
license_ref: ""
---

# Go Wiki: Editors and IDEs for Go

Go Wiki: Editors and IDEs for Go - The Go Programming Language
# Go Wiki: Editors and IDEs for Go
## Popular

The Go Developer Survey <https://go.dev/blog/survey2021-results> showed these as the most popular editors.

-
**Visual Studio Code <https://code.visualstudio.com/>**: Free & open source IDE by Microsoft. Visual Studio Code supports Go syntax highlighting out of the box. Additional features are provided by the official vscode-go <https://github.com/golang/vscode-go> plugin.

-
**GoLand <https://www.jetbrains.com/go/>**: JetBrains’s cross-platform, fully featured <https://www.jetbrains.com/go/features/> Go IDE (commercial). Free for students, teachers, open-source developers, and user-groups (see details <https://www.jetbrains.com/go/buy/#edition=discounts>). Also available as part of IntelliJ IDEA Ultimate.

-
**Vim <http://www.vim.org/>** & **Neovim <https://neovim.io/>**: Vi Improved. There are a number of plugins available that make editing Go code easier.

- The vim-go <https://github.com/fatih/vim-go> plugin includes misc/vim and has many other new improvements.
- ALE <https://github.com/dense-analysis/ale> for linting, async
- coc <https://github.com/neoclide/coc.nvim> for code completion
- The tagbar <https://github.com/majutsushi/tagbar> plugin uses Gotags, above, to show an outline of the current file
- A vim compiler plugin <https://github.com/rjohnsondev/vim-compiler-go> for syntax checking
- A vim-godef <https://github.com/dgryski/vim-godef> plugin integrates with the ‘godef’ tool, above
- A vim-go-extra <https://github.com/vim-jp/vim-go-extra> is vim plugin based on misc/vim in go repository. This works fine on windows too!
- The go-ide <https://github.com/plentiform/go-ide> is a Neovim configuration file that ties go related plugins together making autocomplete, auto-importing, snippets, code formatting, and file search/browsing easier.
- govim <https://github.com/govim/govim> is an LSP-driven vim plugin for Go development, written in Go using Vim8’s channel support.

-
**Emacs <https://www.gnu.org/software/emacs/>**: Extensible and customizable text editor. It has generic LSP support that works well with gopls, the official Go language server.

- **LSP Mode <https://emacs-lsp.github.io/lsp-mode/>** provides LSP support with a batteries-included approach, with many integrations enabled “out of the box” and several additional behaviors provided by lsp-mode itself.
- **Eglot <https://github.com/joaotavora/eglot/blob/master/README.md>** provides LSP support with a minimally-intrusive approach, focusing on smooth integration with other established packages. It provides a few of its own eglot- commands but no additional keybindings by default.
- Mode file maintained at https://github.com/dominikh/go-mode.el <https://github.com/dominikh/go-mode.el>.
- GoFlyMake <https://github.com/dougm/goflymake> Flymake-style syntax checking for Go
- go-errcheck.el <https://github.com/dominikh/go-errcheck.el> Errcheck integration for Emacs
- flycheck-metalinter <https://github.com/favadi/flycheck-gometalinter> Flycheck integration for go-metalinter utility
- go-playground <https://github.com/grafov/go-playground> Local playground inside Emacs
