
## Getting Started

```sh
git clone git@github.com:LucasZapico/adcvart.git
```

### Make Available in Shell 

The binary is `dist/main`, adding the path to this to your shell path will make is available to the CLI.

Add it manually by editing your `~/.bashrc` or `~/.zshrc` file... whatever shell your using. 

```sh 
echo 'alias adcvart='/path/to/dist/main'` >> ~/.bashrc
```

```sh 
echo "alias adcvart='/path/to/dist/main'" >> ~/.zshrc
```


## Development 

Use `pipenv`

```sh
brew install pipenv
```

Let `pipenv` handle the load and start a virtual env
```sh
pipenv shell
```

Install whatever packages are needed to extend the project

```sh
pipenv install <package>
```


## Reference 

[stock adobe leather book](https://stock.adobe.com/images/old-leather-background-with-golden-floral-decoration/22198364)


