from tqdm import tqdm
import json

class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # [1,1,1]   k=2
        # [1,2,3]
        '''
        1 : 1
        2 : 1
        3 : 1
        '''

        k_subarrays_count = 0
        prefix_sum = 0
        prefix_sum_count = {}
        prefix_sum_count[0] = 1

        for i in range(len(nums)):

            # Enter prefix sum in map
            prefix_sum+=nums[i]
            #print(f"prefix_sum:\t{prefix_sum}")

            # Check for subarray with sum k
            # prefix_sum at j - prefix_sum at i - 1 = k
            # The number of occurrences of the above case, gives
            # us the number of subarrays with sum k
            # we can rewrite the above case as 
            # prefix_sum at j - k = prefix_sum at i
            # prefix_sum at j is our current prefix sum
            #print(f"prefix_sum - k:\t{prefix_sum - k}")
            if prefix_sum - k in prefix_sum_count.keys():
                #print(prefix_sum - k)
                k_subarrays_count += prefix_sum_count[prefix_sum - k]

            if prefix_sum in prefix_sum_count.keys():
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] =  1
            
        #print(prefix_sum_count)
        return k_subarrays_count

if __name__ == "__main__":

  tc    = Solution()
  k     = 3
  size  = 150

# Assuming your JSONL file is named 'data.jsonl'
input_file_path = '/home/aftab/workspace/git-repos/gene-subseq-analysis/data/synth_gseq_family/val.jsonl'
output_file_path = 'val_enriched.jsonl'

# Read each line from the JSONL file
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:

    for line in tqdm(infile, desc = 'Read in sequences'):

          json_obj = json.loads(line.strip())
            
          # Access the gene_subsequence field
          gene_subsequence = json_obj.get('gene_subsequence', None)
        
          arr   = gene_subsequence

          arr_T = [0]*size
          arr_G = [0]*size
          arr_C = [0]*size
          arr_A = [0]*size 

          idx = 0
          for a in arr:
              if a == "T":
                arr_T[idx]=1
              if a == "G":
                arr_G[idx]=1
              if a == "C":
                arr_C[idx]=1
              if a == "A":
                arr_A[idx]=1
              idx+=1

          subseqs_T_k3 = tc.subarraySum(arr_T,k)
          subseqs_G_k3 = tc.subarraySum(arr_G,k)
          subseqs_C_k3 = tc.subarraySum(arr_C,k)
          subseqs_A_k3 = tc.subarraySum(arr_A,k)
          
          # Add the new field to the JSON object
          json_obj['subseqs_T_k3'] = subseqs_T_k3
          json_obj['subseqs_G_k3'] = subseqs_G_k3
          json_obj['subseqs_C_k3'] = subseqs_C_k3
          json_obj['subseqs_A_k3'] = subseqs_A_k3

          # Write the modified JSON object to the output file
          outfile.write(json.dumps(json_obj) + '\n')

    print(f"New JSONL file saved as {output_file_path}")


