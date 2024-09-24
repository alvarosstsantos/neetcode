class HistoryElement(object):

    def __init__(self, url):
        """
        :type url: str
        :type prev: HistoryElement
        :type next: HistoryElement
        """
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """

        self.curr = HistoryElement(homepage)

        self.head = HistoryElement("")
        self.tail = HistoryElement("")

        self.curr.next = self.tail
        self.curr.prev = self.head

        self.head.next = self.curr
        self.tail.prev = self.curr

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """

        node = HistoryElement(url)
        node.prev = self.curr
        node.next = self.tail
        self.curr.next = node
        self.curr = node

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        i = 0

        while (self.curr.prev != self.head and i < steps):
            i += 1
            self.curr = self.curr.prev

        return self.curr.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        i = 0

        while (self.curr.next != self.tail and i < steps):
            i += 1
            self.curr = self.curr.next

        return self.curr.url


class EfficientBrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.top = self.curr = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.top = self.curr = self.curr + 1
        self.history = self.history[:self.curr] + [url]

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        self.curr = self.curr - steps if self.curr - steps >= 0 else 0
        return self.history[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        self.curr = self.curr + steps if self.curr + steps <= self.top else self.top
        return self.history[self.curr]


if __name__ == "__main__":

    history = EfficientBrowserHistory("leetcode.com")
    assert history.back(0) == "leetcode.com"
    assert history.back(1) == "leetcode.com"
    assert history.back(2) == "leetcode.com"
    assert history.forward(0) == "leetcode.com"
    assert history.forward(1) == "leetcode.com"
    assert history.forward(2) == "leetcode.com"
    history.visit("google.com")
    history.visit("facebook.com")
    history.visit("youtube.com")
    assert history.back(1) == "facebook.com"
    assert history.back(1) == "google.com"
    assert history.forward(1) == "facebook.com"
    history.visit("linkedin.com")
    assert history.forward(2) == "linkedin.com"
    assert history.back(2) == "google.com"
    assert history.back(7) == "leetcode.com"
    assert history.forward(10) == "linkedin.com"
