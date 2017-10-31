Secure Login
============

For a secure login, you can copy-paste your code from the second
exercise, but this time you'll be hashing passwords.

Use werkzeug's `security` library, which is built in to Flask.

```python3
from werkzeug.security import (
                      generate_password_hash,
                      check_password_hash,
                      )
```

Flask's documentation has [simple, detailed instructions](http://flask.pocoo.org/snippets/54/).
