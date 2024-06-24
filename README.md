# An ML Framework for Gene Subsequence Analysis

In this exploratory work, we try to build an approach to investigate the relationship
between gene subsequences and gene families.

## Synthetic Dataset Details

We apply the approach on a synthetic dataset, where each sample has the following construct:

```
{
	gene_sequence: <>,
        gene_family: <>
}
```

A gene sequence is represented as a sequence of characters, where each character represents
a neocleotide. For our exploratory study, we consider the following neocleotides: A, C, G, T, 
where each of them correspond to the four nucleotide bases of a DNA strand. 
We consider the following gene families: [INS](https://medlineplus.gov/genetics/gene/ins/), [TP53](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/tp53-gene), [HBB](https://medlineplus.gov/genetics/gene/hbb/). 

The synthetic dataset consists of 50,000 samples (40k train, 5k validation, and 5k test samples). 
Each gene sequence consists of 150 characters. Here is an example:

```
{
	gene_sequence: ["A","T",...,"C"],
        gene_family: "INS"
}
```

### Motivation behind Building the Framework

We want to create a machine-learning framework to check if there are relationships between
certain features of gene subsequences and the families of genes.

## Construction of Nucleotide-Count Subsequence Feature from Dataset

We construct the feature *Subs_k_N*, the number of subsequences in a gene
sequence where the total number of neocleotides of type *N* is *k*.  We find
this feature for each nucleotide using a hash-map-based prefix-sum approach.
The complexity of the approach is *O(n)* where *n* is the number of characters
in the given sample.

After adding a feature for each nucleotide for each sample, our sample has the following
fields (a dummy example for k=3):

```
{
	gene_sequence: ["A","T",...,"C"],
        gene_family: "INS",
        subseqs_A_k3: 12,
        subseqs_T_k3: 84,
        subseqs_G_k3: 7,
        subseqs_C_k3: 4
}
```

## Applying ML Algorithms to Analyze Relationship between Gene Subsequence and Family

We build a tool using which different machine learning algorithms can be applied
to predict gene family from nucleotide-count subsequence feature. 

## References

- Wikipedia, Nucleic Acid Sequence [(link)](https://en.wikipedia.org/wiki/Nucleic_acid_sequence)


