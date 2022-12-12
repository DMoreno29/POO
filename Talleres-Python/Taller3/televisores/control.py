class Control:
    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def setCanal(self,canal):
        self._tv.setCanal(canal)