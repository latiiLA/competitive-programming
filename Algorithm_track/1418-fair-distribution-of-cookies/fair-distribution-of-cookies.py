class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        result = float('inf')
        local_ans = [0] * k

        def backtracking(local_ans, cookie_num):
            # base case
            if cookie_num == len(cookies):
                nonlocal result
                result = min(result, max(local_ans))
                return

            # add cookies and back track
            for i in range(k):
                local_ans[i] += cookies[cookie_num]
                backtracking(local_ans, cookie_num + 1)
                local_ans[i] -= cookies[cookie_num]
                if local_ans[i] == 0:
                    break

        backtracking(local_ans, 0)

        return result















        # result = []
        # n = len(cookies)

        # def backtracking(start, comb):

        #     result.append(comb.copy())
        #     # print("result", result)
        #     for i in range(start, n):
        #         comb.append(cookies[i])
        #         # print(comb)
        #         backtracking(i+1, comb)
        #         comb.pop()

        # backtracking(1, [])
        # print(result)


        # total = sum(cookies)
        # ans = [float('inf'), float('inf')]

        # for res in result:
        #     if len(res) == k or len(res) == n - k:
        #         sum_ = sum(res)
        #         print(sum_, total - sum_)
        #         if max(ans) > max(sum_, total - sum_):
        #             ans[0] = sum_
        #             ans[1] = total - sum_



        # return max(ans)