from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List, Optional


class Trie(ABC):
    class TrieNode:
        def __init__(self):
            """Initializes a TrieNode with a dictionary of children and end-of-word marker."""
            self.children: Dict[str, "Trie.TrieNode"] = defaultdict(Trie.TrieNode)
            self.is_end_of_word: bool = False
            self.word: Optional[str] = None

    def __init__(self):
        """Initializes the Trie with a root TrieNode."""
        self._root: Trie.TrieNode = self.TrieNode()

    @property
    def root(self) -> "Trie.TrieNode":
        """Returns the root TrieNode of the Trie."""
        return self._root

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to insert.

        Raises:
            ValueError: If the word is an empty string or contains only whitespace.
        """
        Trie._disallow_empty_string(word, "word")
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    @abstractmethod
    def search(self, query: str) -> Optional[str]:
        """
        Searches for a word in the Trie.

        Args:
            query (str): The word to search for in the Trie.

        Returns:
            Optional[str]: The word if found, otherwise None.

        Raises:
            ValueError: If the query is an empty string or contains only whitespace.
        """
        pass

    def collect_words(self) -> List[str]:
        """
        Collects all words stored in the Trie.

        Returns:
            List[str]: A list of all words in the Trie.
        """
        words: List[str] = []

        def _collect(node: "Trie.TrieNode", prefix: List[str]) -> None:
            if node.is_end_of_word:
                words.append("".join(prefix))
            for char, child in node.children.items():
                prefix.append(char)
                _collect(child, prefix)
                prefix.pop()

        _collect(self.root, [])
        return words

    @staticmethod
    def _disallow_empty_string(query: str, param: str) -> None:
        """
        Raises a ValueError if the provided string is empty or contains only whitespace.

        Args:
            query (str): The string to check.
            param (str): The name of the parameter being checked.

        Raises:
            ValueError: If the string is empty or contains only whitespace.
        """
        if not query.strip():
            raise ValueError(f"`{param}` parameter must be a non-empty string")


class ExactTrie(Trie):
    def search(self, query: str) -> Optional[str]:
        """
        Searches for an exact match of the query in the ExactTrie.

        Args:
            query (str): The word to search for.

        Returns:
            Optional[str]: The word if found, otherwise None.

        Raises:
            ValueError: If the query is an empty string or contains only whitespace.
        """
        Trie._disallow_empty_string(query, "query")
        node = self.root
        for char in query:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.word if node.is_end_of_word else None


class PrefixTrie(Trie):
    def search(self, query: str) -> Optional[str]:
        """
        Searches for a prefix match of the query in the PrefixTrie.

        Args:
            query (str): The prefix to search for.

        Returns:
            Optional[str]: The longest word matching the prefix, or None if no match.

        Raises:
            ValueError: If the query is an empty string or contains only whitespace.
        """
        Trie._disallow_empty_string(query, "query")
        node = self.root
        for char in query:
            if char not in node.children:
                return node.word if node.is_end_of_word else None
            node = node.children[char]
        return node.word


class SuffixTrie(Trie):
    def collect_words(self) -> List[str]:
        """
        Collects all words stored in the SuffixTrie.

        Returns:
            List[str]: A list of all words in the SuffixTrie.
        """
        words: List[str] = []

        def _collect(node: "Trie.TrieNode", suffix: List[str]) -> None:
            if node.is_end_of_word:
                words.append("".join(reversed(suffix)))
            for char, child in node.children.items():
                suffix.append(char)
                _collect(child, suffix)
                suffix.pop()

        _collect(self.root, [])
        return words

    def insert(self, word: str) -> None:
        """
        Inserts a word into the SuffixTrie.

        Args:
            word (str): The word to insert.

        Raises:
            ValueError: If the word is an empty string or contains only whitespace.
        """
        Trie._disallow_empty_string(word, "word")
        node = self.root
        for char in reversed(word):
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, query: str) -> Optional[str]:
        """
        Searches for a suffix match of the query in the SuffixTrie.

        Args:
            query (str): The suffix to search for.

        Returns:
            Optional[str]: The longest word matching the suffix, or None if no match.

        Raises:
            ValueError: If the query is an empty string or contains only whitespace.
        """
        Trie._disallow_empty_string(query, "query")
        node = self.root
        for char in reversed(query):
            if char not in node.children:
                return node.word if node.is_end_of_word else None
            node = node.children[char]
        return node.word
