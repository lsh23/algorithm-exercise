class Solution:
    def solve(self, n: int, k: int, products: list[int]) -> int:

        product_indexes = [[] for _ in range(K + 1)]
        ans: int = 0

        for i in range(K):
            product_indexes[products[i]].append(i)

        # for x in product_indexes:
        #     print(x)

        plugged: list[int] = []

        for i in range(K):

            # print("-----")
            # print(plugged)
            # for idx, v in enumerate(product_indexes):
            #     print(idx ,v)

            if products[i] in plugged:
                product_indexes[products[i]].remove(i)
                continue

            if len(plugged) < N:
                plugged.append(products[i])
                product_indexes[products[i]].remove(i)
                continue

            removed_product: int = -1
            for plugged_product in plugged:
                if not product_indexes[plugged_product]:
                    removed_product = plugged_product
                    break

            if removed_product == -1:
                max_index: int = -1
                for plugged_product in plugged:
                    if max_index < product_indexes[plugged_product][0]:
                        max_index = product_indexes[plugged_product][0]
                        removed_product = plugged_product

            ans += 1
            plugged.remove(removed_product)
            plugged.append(products[i])
            product_indexes[products[i]].remove(i)

        return ans


if __name__ == '__main__':
    N: int
    K: int
    N, K = map(int, input().split())
    products: list[int] = [int(x) for x in input().split()]
    s: Solution = Solution()
    print(s.solve(N, K, products))
