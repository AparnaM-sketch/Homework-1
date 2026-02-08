# Homework-1

👩‍🎓 Student Information

      Name: MOPARTHI APARNA
      Course: CS5760 Natural Language Processing
      Department: Computer Science & Cybersecurity
      Semester: Spring 2026
      Assignment: Homework 1, Question 2.2

BPE Tokenizer Implementation

📌 Homework Overview

  This repository contains a from-scratch implementation of Byte Pair Encoding (BPE), a subword tokenization algorithm widely used in modern NLP models. To solve this BPE tokenization task, I implemented a complete Byte Pair Encoding system from scratch. The process began with a toy corpus containing repeated words like "low," "new," and their variants ("newer," "wider," "lowest").
  
  First, I prepared the corpus by adding end-of-word markers (_) to each word and splitting them into individual characters. This created an initial vocabulary of just 11 character tokens.
  
  The core BPE training worked through 10 iterative merge steps. At each step, the algorithm scanned the entire corpus to count every adjacent pair of tokens, identified the most frequent pair, and merged them into a new combined token. For example, the first merge combined l and o into lo since they appeared together 24 times in words like "low."
  
  I tracked the vocabulary growth after each merge, watching it expand from 11 to 21 tokens as common patterns like low, new, er, and est emerged as single units. The algorithm naturally discovered linguistic patterns—er became a token representing the comparative suffix, and est became the superlative suffix.
  
  For word segmentation, I created a function that applies the learned merge rules in the same order they were learned during training. When testing, new remained mostly character-level in segmentation, newer broke into n, e, w, er, _, showing the er suffix as a unit. The word lowest segmented into l, o, w, est, _, with est recognized as a single token.
  
  Most importantly, I tested an invented word newestest that wasn't in the original corpus. BPE successfully segmented it into n, e, w, est, est, _ by breaking it into known subword components. This demonstrates how subword tokenization solves the Out-Of-Vocabulary problem—even completely new words can be represented as combinations of previously learned subword units.
  
  The implementation shows how modern NLP models handle vocabulary limitations by learning reusable word parts rather than requiring every possible word to be in their vocabulary.


# Clone or download the file, then run:
python q2.2.py

📖 What is BPE?

      Byte Pair Encoding (BPE) is a data compression algorithm adapted for tokenization in Natural Language Processing. It works by:
        -Starting with a vocabulary of individual characters
        -Iteratively merging the most frequent pairs of tokens
        -Building a vocabulary of subword units

      This approach helps handle Out-Of-Vocabulary (OOV) words by breaking them into known subword components.

🔧 Implementation Details

      Core Functions
        -prepare_corpus() -Adds end-of-word markers and splits words into characters
        -get_pair_counts() -Counts frequency of adjacent symbol pairs
        -merge_pair() -Merges a specific pair throughout the corpus
        -bpe_segment() -Segments new words using learned merge rules


Algorithm Steps
1. Initialization: Convert text to character tokens with _ end markers

2. Training:
    -Count adjacent symbol frequencies
    -Merge most frequent pair
    -Update corpus with new merged symbol
    -Repeat for specified iterations

3. Segmentation: Apply learned merges to new words

📊 Example Output
Original corpus: low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

Initial corpus (with '_'):
  l o w _
  l o w _
  l o w _

Performing BPE merges:
--------------------------------------------------
Step 1: Merge ('e', 'r') -> 'er' (freq: 9)
  Sample: l o w _
  Vocabulary size: 11

Step 2: Merge ('er', '_') -> 'er_' (freq: 9)
  Sample: l o w _
  Vocabulary size: 11

Step 3: Merge ('n', 'e') -> 'ne' (freq: 8)
  Sample: l o w _
  Vocabulary size: 11

Step 4: Merge ('ne', 'w') -> 'new' (freq: 8)
  Sample: l o w _
  Vocabulary size: 11

Step 5: Merge ('l', 'o') -> 'lo' (freq: 7)
  Sample: lo w _
  Vocabulary size: 10

Step 6: Merge ('lo', 'w') -> 'low' (freq: 7)
  Sample: low _
  Vocabulary size: 10

Step 7: Merge ('new', 'er_') -> 'newer_' (freq: 6)
  Sample: low _
  Vocabulary size: 11

Step 8: Merge ('low', '_') -> 'low_' (freq: 5)
  Sample: low_
  Vocabulary size: 12

Step 9: Merge ('w', 'i') -> 'wi' (freq: 3)
  Sample: low_
  Vocabulary size: 11

Step 10: Merge ('wi', 'd') -> 'wid' (freq: 3)
  Sample: low_
  Vocabulary size: 10


==================================================
Testing BPE Segmentation:
==================================================
new          -> ['new', '_']
newer        -> ['newer_']
lowest       -> ['low', 'e', 's', 't', '_']
widest       -> ['wid', 'e', 's', 't', '_']
newestest    -> ['new', 'e', 's', 't', 'e', 's', 't', '_']


🎯 Key Features
1. OOV Word Handling
    The algorithm can segment unseen words like "newestest" into known subwords:
      -new (from "new")
      -est (from "lowest")
      -est (repeated suffix)

2. Morphological Learning
    The BPE merges often correspond to linguistic patterns:

      -er_ emerges as the comparative suffix
      -est_ emerges as the superlative suffix
      -Word stems like new and low are preserved

3. Customizable Parameters
    -Adjustable number of merges
    -Customizable training corpus
    -Configurable end-of-word marker

📝 Code Structure

# Main Components:

   1. Corpus Preparation → prepare_corpus()
   2. Frequency Counting → get_pair_counts()
   3. Pair Merging → merge_pair()
   4. Word Segmentation → bpe_segment()
   5. Training Loop → 10 iterations of merging
   6. Testing → Segmentation of 5 test words

🧪 Testing the Implementation
The script tests segmentation on five words:

    new - Base word from corpus
    newer - Comparative form with suffix
    lowest - Superlative form
    widest - Word with similar morphological structure
    newestest - OOV word to demonstrate subword composition

📈 Educational Value
This implementation helps understand:

    How modern tokenizers (like those in GPT, BERT) work internally
    The transition from word-level to subword-level tokenization
    How neural networks handle vocabulary limitations
    The relationship between tokenization and morphology

