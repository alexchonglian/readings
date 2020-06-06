def enum(*args, **kwargs):
    return type("Enum", (object,), dict(zip(args, xrange(len(args))), **kwargs))

Seasons = enum("Spring", "Summer", "Autumn", Winter=1)

print Seasons.Autumn