from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMenu, QMessageBox
from caloriestracker.libcaloriestrackerfunctions import qmessagebox
from caloriestracker.ui.Ui_wdgUsers import Ui_wdgUsers
from logging import debug

class wdgUsers(QWidget, Ui_wdgUsers):
    def __init__(self, mem,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.tblUsers.settings(self.mem, "wdgProducts")
        self.update()

    def update(self):
        self.mem.data.users.qtablewidget(self.tblUsers)
        self.lblFound.setText(self.tr("{} products found").format(self.mem.data.users.length()))

    @pyqtSlot() 
    def on_actionUserDelete_triggered(self):
        if self.users.selected.is_deletable()==False:
            qmessagebox(self.tr("This product can't be removed, because is marked as not remavable"))
            return
            
        reply = QMessageBox.question(None, self.tr('Asking your confirmation'), self.tr("This action can't be undone.\nDo you want to delete this record?"), QMessageBox.Yes, QMessageBox.No)                  
        if reply==QMessageBox.Yes:
            self.users.selected.delete()
            self.mem.con.commit()
            self.mem.data.users.remove(self.users.selected)
            self.update()

    @pyqtSlot() 
    def on_actionUserNew_triggered(self):
        from caloriestracker.ui.frmUsersAdd import frmUsersAdd
        w=frmUsersAdd(self.mem, None, self)
        w.exec_()
        self.update()

    @pyqtSlot() 
    def on_actionUserEdit_triggered(self):
        if self.users.selected.system_company==True:
            qmessagebox(
                self.tr("This is a system company so you can't edit it.") + "\n" +
                self.tr("Please, if it's something wrong with it create an issue at") + "\n" + 
                "https://github.com/turulomio/caloriestracker/issues"+ "\n" +
                self.tr("I'll fix it as soon as posible. ;)")
            )
        elif self.users.selected.system_company==False:
            from caloriestracker.ui.frmUsersAdd import frmUsersAdd
            w=frmUsersAdd(self.mem, self.users.selected, self)
            w.exec_()
            self.update()


    def on_tblUsers_customContextMenuRequested(self,  pos):
        menu=QMenu()
        menu.addAction(self.actionUserNew)
        menu.addAction(self.actionUserDelete)
        menu.addAction(self.actionUserEdit)
        
        #Enabled disabled  
        if self.mem.data.users.selected==None:
            self.actionUserDelete.setEnabled(False)
            self.actionUserEdit.setEnabled(False)
        else:
            self.actionUserDelete.setEnabled(True)
            self.actionUserEdit.setEnabled(True)
        menu.exec_(self.tblUsers.mapToGlobal(pos))

    def on_tblUsers_itemSelectionChanged(self):
        self.users.cleanSelection()
        for i in self.tblUsers.selectedItems():
            if i.column()==0:#only once per row
                self.mem.data.users.selected=self.mem.data.users.arr[i.row()]
        debug("Selected product: " + str(self.mem.data.users.selected))
      