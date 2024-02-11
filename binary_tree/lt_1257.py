class Solution:
    def findSmallestRegion(
        self, regions: list[list[str]], region1: str, region2: str
    ) -> str:
        fatherDict = {}

        for region in regions:
            father, sons = region[0], region[1:]
            for son in sons:
                fatherDict[son] = father

        region1Ancestors = set()

        while region1 in fatherDict:
            region1Ancestors.add(region1)
            region1 = fatherDict[region1]

        while region2 not in region1Ancestors and region2 in fatherDict:
            region2 = fatherDict[region2]

        return region2
