# How to use

* First, download this repository from Github either by downloading it as a ZIP archive (the big green button somewhere at the top of the page), or just `git clone` it

* Fill `profile_ids.txt` with user ids:

```
2638423981
1236715848
1623786238
```

* Paste your VKontakte user token to `user_token.txt`. You can get the token from https://vkhost.github.io . I don't trust that website personally, so be sure to only specify that it should have "access to messages" and "access anytime", nothing more. You will be able to disable this thing in your VK profile's security settings, namely the "Connected apps" section

* Write your message in `message.txt`

* Do either of these:
    * Go into the Poetry shell using `poetry shell` (if you don't know what Poetry is and how to install it, google "Python Poetry"; however, if you don't want to be invested in this, read further)
    * Install dependencies using `pip install {dependency_name}`, where `{dependency_name}` is taken from `pyproject.toml`'s `[tool.poetry.dependencies]` section (you don't have to do it for `python`)
    * Run `poetry run python program.py` (then you don't have to do the next step)

* Run `python program.py`
