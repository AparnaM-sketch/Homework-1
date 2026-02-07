import re
from collections import defaultdict, Counter

def prepare_corpus(text):
    """Prepare initial corpus with characters separated by spaces"""
    words = text.split()
    # Add end-of-word marker and split into characters
    corpus = []
    for word in words:
        # Add '_' and split into characters
        chars = list(word) + ['_']
        corpus.append(' '.join(chars))
    return corpus

def get_pair_counts(corpus):
    """Count frequency of adjacent pairs in the corpus"""
    pairs = defaultdict(int)
    for token in corpus:
        symbols = token.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += 1
    return pairs

def merge_pair(pair, corpus):
    """Merge a pair in the corpus"""
    new_corpus = []
    p0, p1 = pair
    pattern = re.compile(r'(?<!\S)' + re.escape(p0 + ' ' + p1) + r'(?!\S)')
    
    for token in corpus:
        # Replace the pair with merged version
        new_token = pattern.sub(p0 + p1, token)
        new_corpus.append(new_token)
    return new_corpus

# Step 1: Prepare the corpus
corpus_text = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
print("Original corpus:", corpus_text)
print()

# Get initial corpus
corpus = prepare_corpus(corpus_text)
print("Initial corpus (with '_'):")
for item in corpus[:3]:  # Show first 3 for brevity
    print(f"  {item}")
print()

# Step 2: Learn BPE merges
num_merges = 10
merges = []
vocab_history = []

print("Performing BPE merges:")
print("-" * 50)

for step in range(1, num_merges + 1):
    # Get pair counts
    pairs = get_pair_counts(corpus)
    if not pairs:
        break
    
    # Find most frequent pair
    most_freq_pair = max(pairs.items(), key=lambda x: x[1])
    pair, freq = most_freq_pair
    
    # Record the merge
    merges.append(pair)
    
    # Merge the pair
    corpus = merge_pair(pair, corpus)
    
    # Get current vocabulary
    vocab = set()
    for token in corpus:
        vocab.update(token.split())
    
    vocab_history.append(vocab)
    
    # Print step info
    print(f"Step {step}: Merge {pair} -> '{''.join(pair)}' (freq: {freq})")
    print(f"  Sample: {corpus[0]}")
    print(f"  Vocabulary size: {len(vocab)}")
    print()

# Step 3: Create segmenter function
def bpe_segment(word, merges):
    """Segment a word using learned BPE merges"""
    # Start with character-level tokens
    tokens = list(word) + ['_']
    
    # Apply each merge in order
    for merge_pair in merges:
        new_token = merge_pair[0] + merge_pair[1]
        i = 0
        while i < len(tokens) - 1:
            if tokens[i] == merge_pair[0] and tokens[i+1] == merge_pair[1]:
                # Replace the pair
                tokens[i] = new_token
                tokens.pop(i+1)
            else:
                i += 1
    
    return tokens

# Step 4: Test segmentation
print("\n" + "="*50)
print("Testing BPE Segmentation:")
print("="*50)

test_words = ["new", "newer", "lowest", "widest", "newestest"]
for word in test_words:
    segments = bpe_segment(word, merges)
    print(f"{word:12} -> {segments}")