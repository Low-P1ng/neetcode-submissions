class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n]+=1
            if len(dic) <= 2:
                continue

            new_dic = defaultdict(int)
            for n,f in dic.items():
                if f>1:
                    new_dic[n] = f-1
            dic = new_dic

        res = []
        for n in dic.keys():
            if nums.count(n)>len(nums)/3:
                res.append(n)
        return res
