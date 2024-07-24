

# Overview

[Tries](https://en.wikipedia.org/wiki/Trie) are my favorite data structure.
(The [Wagner-Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm) to find Levenshtein-Damerau edit distance is my favorite algorithm; as you can tell, I've got a thing for strings.)
I find myself constantly reaching for tries to perform partial string matching,
and sometimes it's by prefix and sometimes by suffix.

Probably my biggest use case is when I have to process a list of URLs, and I want to determine which URLs
match any of the entries in a list of prefixes or
any of the entries in a list of suffixes.
For example, I might want to process URLs differently depending on their domain (which would be prefix) or the apparent filename in the URL (which would usually be suffix, [query strings and fragments](https://medium.com/@joseph.pyram/9-parts-of-a-url-that-you-should-know-89fea8e11713) not withstanding.)
Tries make these kinds of look-ups very fast.

Prefix searches require very little modification of a basic implementation of a trie.
Suffix searches present a little more of a challenge,
because you want to insert entries into the tries as reversed strings to facilitate the suffix search.
And likewise the queries on a suffix trie will have to be reversed as well.

I like the trie implementation I've rolled here,
so I'm formalizing it in a public repo to share it with anyone who needs it.


# Installation

Install timbos-trie directly from GitHub. (It's not currently on PyPi.)


```bash
pip install git+https://github.com/timoteostewart/timbos-trie.git
```

```bash
pip install --upgrade git+https://github.com/timoteostewart/timbos-trie.git
```

From there, it's as simple as importing via:

```python
import timbos_trie
```

and creating some tries:

```python
prefix_trie = timbos_trie.PrefixTrie()
```


# Roadmap

- [ ] I need to add `delete()` to complement `insert()`.

- [ ] I plan on adding caching as an optional feature.
Both session-only (i.e., in-memory) caching and persistent caching (a file on disk) would be helpful for different use cases.


# Contributing

Contributions are welcome.
Please fork the repo and submit PRs, or you can submit an issue.
Thanks in advance for your interest.


# License

Distributed under the MIT License. See LICENSE for more information.
