# Some of my dotfiles. #
## It is always good to remember that: ##  
I use [Arch](https://archlinux.org "OS") as OS.
[Zsh](https://www.zsh.org/ "Shell") for the shell (with [OMZ](https://ohmyz.sh/ "Shell framework") framework).  
[Qtile](https://qtile.org/ "Desktop Enviroment") as DE.  
[Lightdm](https://github.com/canonical/lightdm "Display manager") for display management.  
[Nitrogen](https://github.com/l3ib/nitrogen "Wallpaper setter") to search and set desktop background wallpapers.  
And a little more, there are some dependencies, like:
## Fonts ##
[Nerd Fonts](https://www.nerdfonts.com/ "Nerd fonts") specifically "Hack nerd font" & "Symbols nerd font", these are used on the DE for symbols and more.
[Hack fonts](https://sourcefoundry.org/hack/ "Hack fonts") for vscode, terminal and everything that need an "easy read".
[Hack fonts](https://github.com/tonsky/FiraCode "Fira Code Fonts) for programming ligatures.  
There are some fonts that are not listed because they are no fundamental for my UI. Those are "user picks".

## OMZ ##
When cloning my dotfiles, there are submodules like my OMZ files, you will need to run some commands to make this work:
```sh
git submodule update --init
cd oh-my-zsh
git submodule update --init
```
Afterwards, you can link my zshrc in your home to get everything running correctly:
```sh
ln -s zshrc ~/.zshrc
```