# Anagram

---

* An anagram is a word, phrase, or name formed by rearranging the letters of another. 
* Example: cinema and iceman
* Build a function that will take in a string as it's first argument, and an unknown amount of arguments afterwards. `(hmmm if only there was a way in Python we can use something for an unknown amount of arguments)`
* The first argument will be our main string/word. 
* Any further arguments that are given will be checked against the first argument to see if it is a anagram.
* If no anagrams exist return `false`
* Otherwise return all arguments that are anagrams
* Example:

```
is_anagram("ant", "tan", "stand", "nut", "buffalo", "nat") == ["tan", "nat"]

is_anagram("building", "hello", "world") == False
```

***NOTE***

* For this homework don't worry about spaces, or special characters. 
* Assume we are only assessing strings that are one word each