    def find_all(self, name=None, attrs={}, recursive=True, text=None,
                 limit=None, **kwargs):
        """Extracts a list of Tag objects that match the given
        criteria.  You can specify the name of the Tag and any
        attributes you want the Tag to have.

        The value of a key-value pair in the 'attrs' map can be a
        string, a list of strings, a regular expression object, or a
        callable that takes a string and returns whether or not the
        string matches for some custom definition of 'matches'. The
        same is true of the tag name."""

        generator = self.descendants
        if not recursive:
            generator = self.children
        return self._find_all(name, attrs, text, limit, generator, **kwargs)
    findAll = find_all       # BS3
    findChildren = find_all  # BS2
