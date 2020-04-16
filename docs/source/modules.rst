Test
====

def as_chan(create_chan):
    ```
    Decorator which creates channel and coroutine.
    Passes channel as a first value to coroutine and returns that channel.
    ```
    Usage:

    .. code-block:: python

        @as_chan
        def thermo(chan, unit):
            while True:
                yield chan.put(convert(thermo_get(), unit))

        @coroutine
        def main():
            thermo_chan = thermo('C')
            while True:
                print((yield thermo_chan.get()))  # prints current temperature

    :param create_chan: Type of channel.
    :type create_chan: type[Channel]
    :returns: Created coroutine.



.. toctree::
   :maxdepth: 4

