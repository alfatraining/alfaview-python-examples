# Sample business logic for the alfaview platform for Python

## Reference documentation

- gRPC Python quickstart: http://www.grpc.io/docs/quickstart/python.html
- generated code for Protocol buffers: https://developers.google.com/protocol-buffers/docs/reference/python-generated


## Prerequisites

It is preferred to use virtualenv if possible:
```
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
```

Ensure you have pip > 19 (`pip --version`).

Upgrade via:
```
python -m pip install --upgrade pip
```

A simple `make init` will then install the required packages.


## Supported Python versions

This project is tested via GitLab CI in the following environments:
- Linux (via Docker): Python 2.7 and 3.7
