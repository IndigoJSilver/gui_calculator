## Contributing

First off, thank you for considering contributing to GUI_CALCULATOR. It's people
like you that make GUI_CALCULATOR such a great tool.

### Where do I go from here?

If you've noticed a bug or have a feature request, [make one][new issue]! It's
generally best if you get confirmation of your bug or approval for your feature
request this way before starting to code.

If you have a general question about activeadmin, you can post it on [Stack
Overflow], the issue tracker is only for bugs and feature requests.

### Fork & create a branch

If this is something you think you can fix, then [fork GUI_CALCULATOR] and create
a branch with a descriptive name.

A good branch name would be (where issue #10 is the ticket you're working on):

```sh
git checkout -b 10-add-calculator-recovery
```

### Get the test suite running

Make sure you're making calculator, install PyQt5 using pip

You'll also need python(3.4) installed in order to run scenarios.

Now install the development dependencies:

```sh
pip install pyqt5
```

Then install pyqt5-tools

```sh
pip install pyqt5-tools
```

if you install successed, go to the python console, check that module installed normally.

if module installed normally

```sh
>>> import PyQt5
```

if module installed not normally

```sh
>>> import PyQt5
Traceback (most recent call last):

  File "<input>", line 1, in <module>

  File "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1\plugins\python-ce\helpers\pydev\_pydev_bundle\pydev_import_hook.py", line 21, in do_import

    module = self._system_import(name, *args, **kwargs)

ModuleNotFoundError: No module named 'PyQt5'
```

**Warning** SCSS assets are aimed to be used indifferently with Sprockets **and** webpacker.
As such, make sure not to use any sass-rails directives such as `asset-url` or `image-url`.

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help;
everyone is a beginner at first :smile_cat:

### Get the style right

Your patch should follow the same conventions & pass the same code quality
checks as the rest of the project. `bin/rake lint` will give you feedback in
this regard. You can check & fix style issues by running each linter
individually. Run `bin/rake -T lint` to see the available linters.

### Make a Pull Request

At this point, you should switch back to your master branch and make sure it's
up to date with master branch:

```sh
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 10-add-calculator-recovery
git rebase master
git push --set-upstream origin 10-add-calculator-recovery
```

Finally, go to GitHub and [make a Pull Request][] :D

Github Actions will run our test suite against all supported Rails versions. We
care about quality, so your PR won't be merged until all tests pass. It's
unlikely, but it's possible that your changes pass tests in one Rails version
but fail in another. In that case, you'll have to setup your development
environment (as explained in step 3) to use the problematic Rails version, and
investigate what's going on!

### Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code
has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good][git rebasing]
[resources][interactive rebase] but here's the suggested workflow:

```sh
git checkout 10-add-calculator-recovery
git pull --rebase upstream master
git push --force-with-lease 10-add-calculator-recovery
```

### Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

* It is passing CI.
* It has been approved by at least two maintainers. If it was a maintainer who
  opened the PR, only one extra approval is needed.
* It has no requested changes.
* It is up to date with current master.

Any maintainer is allowed to merge a PR if all of these conditions are
met.
