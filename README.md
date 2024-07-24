# llama3.1-telethon
llama3.1 8B ai on telethon telegram robot without hf token

![l](https://github.com/aDarkDev/llama3.1-telethon/blob/982960f8794306b07d17031648400a9d97a1d177/shot.png)

Note that this robot also works with `cpu` and has been tested and has no problems.

Recommended server specifications: 

Ram: `8GB`

CPU: `2 core`

System: `ubuntu 22 linux`

## Installation
install [ollama](https://ollama.com/) and pull [llama3.1-8b](https://ollama.com/library/llama3.1:8b)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
```bash
ollama pull llama3.1
```

install telethon and other libraries

```bash
pip3 install telethon
pip3 install langchain
pip3 install langchain-ollama
```

Done! now run the script dont forget to put api token in it.

```bash
python3 main.py
```

### Thank you for reading repository this far
