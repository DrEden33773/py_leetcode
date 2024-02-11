import re


class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        return list(
            filter(
                None, re.sub("//.*|/\*(.|\n)*?\*/", "", "\n".join(source)).split("\n")
            )
        )
