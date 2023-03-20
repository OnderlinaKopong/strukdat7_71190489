class Browser:
    def __init__(self):
        self.riwayat = [] 
        self.tampilan = -1 
    def go(self, url):
        while len(self.riwayat) > self.tampilan+1:
            self.riwayat.pop()
        self.riwayat.append(url) 
        self.tampilan += 1 
    def back(self):
        if self.tampilan > 0:
            self.tampilan -= 1 
            return self.riwayat[self.tampilan] 
        return None 
    def forward(self):
        if self.tampilan < len(self.riwayat)-1:
            self.tampilan += 1 
            return self.riwayat[self.tampilan] 
        return None 
    def printAll(self):
        for url in self.riwayat:
            print(url)


browser = Browser()

browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")

print(browser.back()) # output: https://ukdw.ac.id
print(browser.back()) # output: https://google.com
print(browser.forward()) # output: https://ukdw.ac.id

browser.go("https://twitter.com")
browser.printAll() # output: https://google.com https://ukdw.ac.id https://twitter.com