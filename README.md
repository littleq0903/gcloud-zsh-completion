gcloud-zsh-completion
=====================

Z Shell auto completion for Google Cloud SDK

demo: https://asciinema.org/a/8185

![gcloud-zsh-completion](https://f.cloud.github.com/assets/374786/2430363/a329fad8-acd7-11e3-83ac-d626449568e9.png)

## Features

* Auto completion for the following command in Google Cloud SDK
  - gcloud
  - appcfg.py

### Special Completion

* gcloud
  - `gcloud config set ` will be completed by property names
  - `gcloud config set account ` will be completed by your authorized Google account


## Installation

### for zsh experts

Just pull all files in src to your completion (e.g `$fpath`).

### for zsh beginners

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

## Arthors

* Colin Su - https://github.com/littleq0903

## Contribution

### Feature Request

Please open an issue and describe what you expected to see in gcloud-zsh-completion

### Pull Request

Pull requests are welcome, please do remember attach your name to both README.md and the beginning of the file you modified.
