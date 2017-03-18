import sys
from PySide.QtCore import *
from PySide.QtGui import *
import inspect

def guisave(self):

  # Save geometry
    self.settings.setValue('size', self.size())
    self.settings.setValue('pos', self.pos())

    for name, obj in inspect.getmembers(self):
      # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
      if isinstance(obj, QComboBox):
          name = obj.objectName()  # get combobox name
          index = obj.currentIndex()  # get current index from combobox
          text = obj.itemText(index)  # get the text for current index
          self.settings.setValue(name, text)  # save combobox selection to registry

      if isinstance(obj, QLineEdit):
          name = obj.objectName()
          value = obj.text()
          self.settings.setValue(name, value)  # save ui values, so they can be restored next time

      if isinstance(obj, QCheckBox):
          name = obj.objectName()
          state = obj.isChecked()
          self.settings.setValue(name, state)

      if isinstance(obj, QRadioButton):
          name = obj.objectName()
          value = obj.isChecked()  # get stored value from registry
          self.settings.setValue(name, value)

      if isinstance(obj, QGroupBox):
          name = obj.objectName()
          value = obj.isChecked()  # get stored value from registry
          self.settings.setValue(name, value)

def guirestore(self):

    for name, obj in inspect.getmembers(self):

        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = self.settings.value(name)
            # value = unicode(self.settings.value(name).toString())  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QGroupBox):
            name = obj.objectName()
            value = self.settings.value(name)   # get stored value from registry
            value = True if value == 'true' else False
            if value != None:
                obj.setChecked(value)   # restore checkbox

        if isinstance(obj, QComboBox):
            index = obj.currentIndex()  # get current region from combobox
            # text   = obj.itemText(index)   # get the text for new selected index
            name = obj.objectName()
            value = self.settings.value(name)
            if value == "":
                continue
            # get the corresponding index for specified string in combobox
            index = obj.findText(value)

            if index == -1:  # add to list if not found
                obj.insertItems(0, [value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                # preselect a combobox value by index
                obj.setCurrentIndex(index)

        if isinstance(obj, QRadioButton):
            name = obj.objectName()
            value = self.settings.value(name)   # get stored value from registry
            value = True if value == 'true' else False
            if value != None:
                obj.setChecked(value)

        if isinstance(obj, QCheckBox):
            name = obj.objectName()
            value = self.settings.value(name).toBool()  # get stored value from registry
            if value != None:
                obj.setChecked(value)  # restore checkbox
