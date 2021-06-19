# 10.33:  Featured module:  textwrap.

import textwrap

text = ("This is some really long text that we would like to wrap.  "
        "Wouldn't you know it, there's a module for that!  ")


items = textwrap.wrap(text, 10)

print('\n'.join(items))

