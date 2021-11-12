# ML-Dev-Utils

You can find the documentation [here](https://ltu-machine-learning.github.io/ML-Dev-Utils/).

## Development

### Build and publish

You can build the client package by:

```bash
python -m build --sdist --wheel .
```

You can check the build with

```bash
twine check dist/*
tar tzf dist/ml-dev-utils-0.0.1.tar.gz

pip list

$ python
>>> from ml_dev_utils import log_handler
>>> print(log_handler.console)
```

(ml_dev_mcp_client.egg-info/ is hidden by VSC - see .vscode/settings.json)

You can publish the package on PyPI: Double-check for everything before publish!

Once published versions of a package will stay forever.

Even if you delete a package or package version, it's not possible to publish it again.

Therefore do a test publish on test pypi.

```bash
twine upload --repository testpypi dist/*
```

Ready for real publishing - double check again!

```bash
twine upload dist/*
```

### Create documenation

```bash
sphinx-apidoc -fMeET -o /home/vscode/workspace/docs_src/api/ /home/vscode/workspace/src/ml_dev_utils/
sphinx-build -a -b html /home/vscode/workspace/docs_src/ /home/vscode/workspace/docs/
```
