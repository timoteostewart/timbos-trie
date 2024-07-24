from timbos_trie.Trie import ExactTrie, PrefixTrie, SuffixTrie

# run tests from root dir:
# python -m unittest discover ./tests


def main():
    # Example Usage
    prefix_trie = PrefixTrie()
    prefix_trie.insert("apple")
    prefix_trie.insert("applet")

    queries = [
        "app",
        "appl",
        "apple",
        "apples",
        "applet",
        "applets",
        "banana",
    ]

    for q in queries:
        res = prefix_trie.search(q)
        print(q, res)

    print("prefix trie contents:", prefix_trie.collect_words())
    print()

    suffix_trie = SuffixTrie()
    suffix_trie.insert("apple")
    suffix_trie.insert("snapple")

    queries = [
        "ple",
        "pple",
        "apple",
        "zapple",
        "snapple",
        "qqqsnapple",
        "zapples",
        "snapples",
        "banana",
    ]

    for q in queries:
        res = suffix_trie.search(q)
        print(q, res)

    print("suffix trie contents:", suffix_trie.collect_words())
    print()

    exact_trie = ExactTrie()
    exact_trie.insert("aaaa")
    exact_trie.insert("bbbb")
    exact_trie.insert("cccc")
    exact_trie.insert("dddd")

    queries = [
        "aaaa",
        "xaaaa",
        "aaaax",
        "xaaaax",
        "aaa",
        "aaaaa",
        "bbbb",
        "zzzz",
    ]

    for q in queries:
        res = exact_trie.search(q)
        print(q, res)

    print("exact trie contents:", exact_trie.collect_words())
    print()


if __name__ == "__main__":
    main()
