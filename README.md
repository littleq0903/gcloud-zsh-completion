gcloud-zsh-completion
=====================

Z Shell auto completion for Google Cloud SDK

demo: https://asciinema.org/a/8185


## Installation

for zsh experts:

Just pull all files in src to your completion (e.g `$fpath`).

for zsh beginners:

First, added src folder under your `$fpath`:

```shell
fpath=(path/to/gcloud-zsh-completion/src $fpath)
```

if you haven't activate compdef and compinit mods in your `.zshrc`:

```shell
autoload -U compinit compdef
compinit
```

> Remember, your fpath configuration need to be set up before you called `compinit`.

