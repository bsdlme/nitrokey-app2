from typing import Optional

from pynitrokey.nk3.admin_app import InitStatus
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QWidget

from nitrokeyapp.device_data import DeviceData
from nitrokeyapp.information_box import InfoBox
from nitrokeyapp.qt_utils_mix_in import QtUtilsMixIn
from nitrokeyapp.ui.settings_tab import Ui_StettingTab
from nitrokeyapp.worker import Worker


class SettingsTab(QtUtilsMixIn, QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        QWidget.__init__(self, parent)
        QtUtilsMixIn.__init__(self)

        self.data: Optional[DeviceData] = None
        self.ui = Ui_StettingTab()
        self.ui.setupUi(self)

    @property
    def title(self) -> str:
        return "Settings"

    @property
    def widget(self) -> QWidget:
        return self

    @property
    def worker(self) -> Optional[Worker]:
       return None

    def reset(self) -> None:
        self.data = None

    def refresh(self, data: DeviceData) -> None:
        if data == self.data:
            return
        self.reset()
        self.data = data
        if data.status.variant is None:
            return