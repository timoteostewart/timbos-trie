import unittest

import timbos_trie.Trie as Trie


class TestTrie(unittest.TestCase):
    pass


class TestPrefixTrie(TestTrie):
    def test_insert(self):
        prefix_trie = Trie.PrefixTrie()
        prefix_trie.insert("apple")
        prefix_trie.insert("applet")
        self.assertEqual(
            prefix_trie.root.children["a"]
            .children["p"]
            .children["p"]
            .children["l"]
            .children["e"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            prefix_trie.root.children["a"]
            .children["p"]
            .children["p"]
            .children["l"]
            .children["e"]
            .word,
            "apple",
        )
        self.assertEqual(
            prefix_trie.root.children["a"]
            .children["p"]
            .children["p"]
            .children["l"]
            .children["e"]
            .children["t"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            prefix_trie.root.children["a"]
            .children["p"]
            .children["p"]
            .children["l"]
            .children["e"]
            .children["t"]
            .word,
            "applet",
        )

    def test_collect_words(self):
        prefix_trie1 = Trie.PrefixTrie()
        prefix_trie1.insert("apple")
        self.assertEqual(prefix_trie1.collect_words(), ["apple"])

        prefix_trie2 = Trie.PrefixTrie()
        prefix_trie2.insert("apple")
        prefix_trie2.insert("applet")
        self.assertEqual(prefix_trie2.collect_words(), ["apple", "applet"])

    def test_search(self):
        prefix_trie = Trie.PrefixTrie()
        prefix_trie.insert("apple")
        prefix_trie.insert("applet")
        self.assertEqual(prefix_trie.search("app"), None)
        self.assertEqual(prefix_trie.search("appl"), None)
        self.assertEqual(prefix_trie.search("apple"), "apple")
        self.assertEqual(prefix_trie.search("apples"), "apple")
        self.assertEqual(prefix_trie.search("applet"), "applet")
        self.assertEqual(prefix_trie.search("applets"), "applet")

    def test_add_member_empty_string(self):
        prefix_trie = Trie.PrefixTrie()
        with self.assertRaises(ValueError):
            prefix_trie.insert("")

    def test_search_empty_string(self):
        prefix_trie = Trie.PrefixTrie()
        with self.assertRaises(ValueError):
            prefix_trie.search("")


class TestSuffixTrie(TestTrie):
    def test_insert(self):
        suffix_trie = Trie.SuffixTrie()
        suffix_trie.insert("apple")
        suffix_trie.insert("snapple")
        self.assertEqual(
            suffix_trie.root.children["e"]
            .children["l"]
            .children["p"]
            .children["p"]
            .children["a"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            suffix_trie.root.children["e"]
            .children["l"]
            .children["p"]
            .children["p"]
            .children["a"]
            .word,
            "apple",
        )
        self.assertEqual(
            suffix_trie.root.children["e"]
            .children["l"]
            .children["p"]
            .children["p"]
            .children["a"]
            .children["n"]
            .children["s"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            suffix_trie.root.children["e"]
            .children["l"]
            .children["p"]
            .children["p"]
            .children["a"]
            .children["n"]
            .children["s"]
            .word,
            "snapple",
        )

    def test_collect_words(self):
        suffix_trie1 = Trie.SuffixTrie()
        suffix_trie1.insert("apple")
        self.assertEqual(suffix_trie1.collect_words(), ["apple"])

        suffix_trie2 = Trie.SuffixTrie()
        suffix_trie2.insert("apple")
        suffix_trie2.insert("snapple")
        self.assertEqual(suffix_trie2.collect_words(), ["apple", "snapple"])

    def test_search(self):
        suffix_trie = Trie.SuffixTrie()
        suffix_trie.insert("apple")
        suffix_trie.insert("snapple")
        self.assertEqual(suffix_trie.search("ple"), None)
        self.assertEqual(suffix_trie.search("pple"), None)
        self.assertEqual(suffix_trie.search("apple"), "apple")
        self.assertEqual(suffix_trie.search("apples"), None)
        self.assertEqual(suffix_trie.search("zapple"), "apple")
        self.assertEqual(suffix_trie.search("snapple"), "snapple")

    def test_add_member_empty_string(self):
        suffix_trie = Trie.SuffixTrie()
        with self.assertRaises(ValueError):
            suffix_trie.insert("")

    def test_search_empty_string(self):
        suffix_trie = Trie.SuffixTrie()
        with self.assertRaises(ValueError):
            suffix_trie.search("")


class TestExactTrie(TestTrie):
    def test_insert(self):
        exact_trie = Trie.ExactTrie()
        exact_trie.insert("aaaa")
        exact_trie.insert("bbbb")
        self.assertEqual(
            exact_trie.root.children["a"]
            .children["a"]
            .children["a"]
            .children["a"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            exact_trie.root.children["a"]
            .children["a"]
            .children["a"]
            .children["a"]
            .word,
            "aaaa",
        )
        self.assertEqual(
            exact_trie.root.children["b"]
            .children["b"]
            .children["b"]
            .children["b"]
            .is_end_of_word,
            True,
        )
        self.assertEqual(
            exact_trie.root.children["b"]
            .children["b"]
            .children["b"]
            .children["b"]
            .word,
            "bbbb",
        )

    def test_collect_words(self):
        exact_trie1 = Trie.SuffixTrie()
        exact_trie1.insert("aaaa")
        self.assertEqual(exact_trie1.collect_words(), ["aaaa"])

        exact_trie2 = Trie.SuffixTrie()
        exact_trie2.insert("aaaa")
        exact_trie2.insert("bbbb")
        self.assertEqual(exact_trie2.collect_words(), ["aaaa", "bbbb"])

    def test_search(self):
        exact_trie = Trie.ExactTrie()
        exact_trie.insert("aaaa")
        exact_trie.insert("bbbb")
        self.assertEqual(exact_trie.search("aaaa"), "aaaa")
        self.assertEqual(exact_trie.search("xaaaa"), None)
        self.assertEqual(exact_trie.search("aaaax"), None)
        self.assertEqual(exact_trie.search("xaaaax"), None)
        self.assertEqual(exact_trie.search("bbbb"), "bbbb")
        self.assertEqual(exact_trie.search("xbbbb"), None)
        self.assertEqual(exact_trie.search("bbbbx"), None)
        self.assertEqual(exact_trie.search("xbbbbx"), None)

    def test_add_member_empty_string(self):
        exact_trie = Trie.ExactTrie()
        with self.assertRaises(ValueError):
            exact_trie.insert("")

    def test_search_empty_string(self):
        exact_trie = Trie.ExactTrie()
        with self.assertRaises(ValueError):
            exact_trie.search("")


if __name__ == "__main__":
    unittest.main()
