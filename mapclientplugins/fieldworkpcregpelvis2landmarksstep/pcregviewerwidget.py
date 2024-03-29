'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os

os.environ['ETS_TOOLKIT'] = 'qt5'

from PySide6.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt
from PySide6.QtCore import QThread, Signal

from mapclientplugins.fieldworkpcregpelvis2landmarksstep.ui_pcregviewerwidget import Ui_Dialog
from traits.api import HasTraits, Instance, on_trait_change, \
    Int, Dict

from gias3.mapclientpluginutilities.viewers import MayaviViewerObjectsContainer, MayaviViewerLandmark, MayaviViewerFieldworkModel, colours

import copy

REGMODES = {'PC': 1,
            'Linear Scaling': 2,
            }


class _ExecThread(QThread):
    finalUpdate = Signal(tuple)
    update = Signal(tuple)

    def __init__(self, func):
        QThread.__init__(self)
        self.func = func

    def run(self):
        output = self.func(self.update)
        self.finalUpdate.emit(output)


class MayaviPCRegViewerWidget(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''
    defaultColor = colours['bone']
    objectTableHeaderColumns = {'Visible': 0}
    backgroundColour = (0.0, 0.0, 0.0)
    _modelRenderArgs = {}
    _modelDisc = [10, 10]
    _landmarkRenderArgs = {'mode': 'sphere', 'scale_factor': 20.0, 'color': (0, 1, 0)}

    def __init__(self, landmarks, model, config, regFunc, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._scene = self._ui.MayaviScene.visualisation.scene
        self._scene.background = self.backgroundColour

        self.selectedObjectName = None
        self._landmarks = landmarks
        self._landmarkNames = ['none', ]
        self._landmarkNames = self._landmarkNames + sorted(self._landmarks.keys())
        self._origModel = model
        self._regFunc = regFunc
        self._config = config

        self._worker = _ExecThread(self._regFunc)
        self._worker.finalUpdate.connect(self._regUpdate)
        self._worker.update.connect(self._updateMeshGeometry)

        # print 'init...', self._config

        ### FIX FROM HERE ###
        # create self._objects
        self._initViewerObjects()
        self._setupGui()
        self._makeConnections()
        self._initialiseObjectTable()
        self._initialiseSettings()
        self._refresh()

        self._modelRow = None

        # self.testPlot()
        # self.drawObjects()
        print('finished init...', self._config)

    def _initViewerObjects(self):
        self._objects = MayaviViewerObjectsContainer()
        self._objects.addObject('pelvis mesh',
                                MayaviViewerFieldworkModel('pelvis mesh',
                                                           copy.deepcopy(self._origModel),
                                                           self._modelDisc,
                                                           render_args=self._modelRenderArgs
                                                           )
                                )
        # 'none' is first elem in self._landmarkNames, so skip that
        for ln in self._landmarkNames[1:]:
            self._objects.addObject(ln, MayaviViewerLandmark(ln,
                                                             self._landmarks[ln],
                                                             render_args=self._landmarkRenderArgs
                                                             )
                                    )

    def _setupGui(self):
        self._ui.screenshotPixelXLineEdit.setValidator(QIntValidator())
        self._ui.screenshotPixelYLineEdit.setValidator(QIntValidator())
        self._ui.comboBoxRegMode.addItem('PC')
        self._ui.comboBoxRegMode.addItem('Linear Scaling')
        self._ui.spinBoxNPCs.setSingleStep(1)
        for l in self._landmarkNames:
            self._ui.comboBoxLASIS.addItem(l)
            self._ui.comboBoxRASIS.addItem(l)
            self._ui.comboBoxLPSIS.addItem(l)
            self._ui.comboBoxRPSIS.addItem(l)
            self._ui.comboBoxSacral.addItem(l)
            self._ui.comboBoxLHJC.addItem(l)
            self._ui.comboBoxRHJC.addItem(l)

    def _makeConnections(self):
        self._ui.tableWidget.itemClicked.connect(self._tableItemClicked)
        self._ui.tableWidget.itemChanged.connect(self._visibleBoxChanged)
        self._ui.screenshotSaveButton.clicked.connect(self._saveScreenShot)

        self._ui.regButton.clicked.connect(self._worker.start)
        self._ui.regButton.clicked.connect(self._regLockUI)

        self._ui.resetButton.clicked.connect(self._reset)
        self._ui.abortButton.clicked.connect(self._abort)
        self._ui.acceptButton.clicked.connect(self._accept)

        self._ui.comboBoxLASIS.activated.connect(self._updateConfigLASIS)
        self._ui.comboBoxRASIS.activated.connect(self._updateConfigRASIS)
        self._ui.comboBoxLPSIS.activated.connect(self._updateConfigLPSIS)
        self._ui.comboBoxRPSIS.activated.connect(self._updateConfigRPSIS)
        self._ui.comboBoxSacral.activated.connect(self._updateConfigSacral)
        self._ui.comboBoxRHJC.activated.connect(self._updateConfigLHJC)
        self._ui.comboBoxLHJC.activated.connect(self._updateConfigRHJC)

        self._ui.comboBoxRegMode.activated.connect(self._updateConfigRegMode)
        self._ui.spinBoxNPCs.valueChanged.connect(self._updateConfigNPCs)

    def _initialiseSettings(self):

        self._ui.comboBoxRegMode.setCurrentIndex(self._config['regMode'] - 1)
        self._ui.spinBoxNPCs.setValue(self._config['npcs'])

        if self._config['LASIS'] in self._landmarkNames:
            self._ui.comboBoxLASIS.setCurrentIndex(self._landmarkNames.index(self._config['LASIS']))
        else:
            self._ui.comboBoxLASIS.setCurrentIndex(0)

        if self._config['RASIS'] in self._landmarkNames:
            self._ui.comboBoxRASIS.setCurrentIndex(self._landmarkNames.index(self._config['RASIS']))
        else:
            self._ui.comboBoxRASIS.setCurrentIndex(0)

        if self._config['LPSIS'] in self._landmarkNames:
            self._ui.comboBoxLPSIS.setCurrentIndex(self._landmarkNames.index(self._config['LPSIS']))
        else:
            self._ui.comboBoxLPSIS.setCurrentIndex(0)

        if self._config['RPSIS'] in self._landmarkNames:
            self._ui.comboBoxRPSIS.setCurrentIndex(self._landmarkNames.index(self._config['RPSIS']))
        else:
            self._ui.comboBoxRPSIS.setCurrentIndex(0)

        if self._config['Sacral'] in self._landmarkNames:
            self._ui.comboBoxSacral.setCurrentIndex(self._landmarkNames.index(self._config['Sacral']))
        else:
            self._ui.comboBoxSacral.setCurrentIndex(0)

        if self._config['LHJC'] in self._landmarkNames:
            self._ui.comboBoxLHJC.setCurrentIndex(self._landmarkNames.index(self._config['LHJC']))
        else:
            self._ui.comboBoxLHJC.setCurrentIndex(0)

        if self._config['RHJC'] in self._landmarkNames:
            self._ui.comboBoxRHJC.setCurrentIndex(self._landmarkNames.index(self._config['RHJC']))
        else:
            self._ui.comboBoxRHJC.setCurrentIndex(0)

    def _initialiseObjectTable(self):
        self._ui.tableWidget.setRowCount(self._objects.getNumberOfObjects())
        self._ui.tableWidget.verticalHeader().setVisible(False)
        self._ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        r = 0
        # 'none' is first elem in self._landmarkNames, so skip that
        for ln in self._landmarkNames[1:]:
            self._addObjectToTable(r, ln, self._objects.getObject(ln))
            r += 1

        self._addObjectToTable(r, 'pelvis mesh', self._objects.getObject('pelvis mesh'), checked=True)
        self._modelRow = r
        self._ui.tableWidget.resizeColumnToContents(self.objectTableHeaderColumns['Visible'])

    def _addObjectToTable(self, row, name, obj, checked=True):
        typeName = obj.typeName
        print('adding to table: %s (%s)' % (name, typeName))
        tableItem = QTableWidgetItem(name)
        if checked:
            tableItem.setCheckState(Qt.Checked)
        else:
            tableItem.setCheckState(Qt.Unchecked)

        self._ui.tableWidget.setItem(row, self.objectTableHeaderColumns['Visible'], tableItem)

    def _tableItemClicked(self):
        selectedRow = self._ui.tableWidget.currentRow()
        self.selectedObjectName = self._ui.tableWidget.item(
            selectedRow,
            self.objectTableHeaderColumns['Visible']
        ).text()
        print(selectedRow)
        print(self.selectedObjectName)

    def _visibleBoxChanged(self, tableItem):
        # get name of object selected
        # name = self._getSelectedObjectName()

        # checked changed item is actually the checkbox
        if tableItem.column() == self.objectTableHeaderColumns['Visible']:
            # get visible status
            name = tableItem.text()
            visible = tableItem.checkState().name == 'Checked'

            print('visibleboxchanged name', name)
            print('visibleboxchanged visible', visible)

            # toggle visibility
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _getSelectedObjectName(self):
        return self.selectedObjectName

    def _getSelectedScalarName(self):
        return 'none'

    def drawObjects(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).draw(self._scene)

    def _updateConfigLASIS(self):
        self._config['LASIS'] = self._ui.comboBoxLASIS.currentText()

    def _updateConfigRASIS(self):
        self._config['RASIS'] = self._ui.comboBoxRASIS.currentText()

    def _updateConfigLPSIS(self):
        self._config['LPSIS'] = self._ui.comboBoxLPSIS.currentText()

    def _updateConfigRPSIS(self):
        self._config['RPSIS'] = self._ui.comboBoxRPSIS.currentText()

    def _updateConfigSacral(self):
        self._config['Sacral'] = self._ui.comboBoxSacral.currentText()

    def _updateConfigLHJC(self):
        self._config['LHJC'] = self._ui.comboBoxLHJC.currentText()

    def _updateConfigRHJC(self):
        self._config['RHJC'] = self._ui.comboBoxRHJC.currentText()

    def _updateConfigRegMode(self):
        self._config['regMode'] = REGMODES[self._ui.comboBoxRegMode.currentText()]

    def _updateConfigNPCs(self):
        self._config['npcs'] = self._ui.spinBoxNPCs.value()

    def _updateMeshGeometry(self, P):
        meshObj = self._objects.getObject('pelvis mesh')
        meshObj.updateGeometry(P.reshape((3, -1, 1)), self._scene)

    def _regUpdate(self, output):
        regModel, RMSE, T = output
        # update error field
        self._ui.lineEditRMSE.setText('{:12.10f}'.format(RMSE))
        self._ui.lineEditTransformation.setText(', '.join(['{:5.2f}'.format(t) for t in T]))

        # unlock reg ui
        self._regUnlockUI()

    def _regLockUI(self):
        self._ui.comboBoxRegMode.setEnabled(False)
        self._ui.spinBoxNPCs.setEnabled(False)
        self._ui.comboBoxLASIS.setEnabled(False)
        self._ui.comboBoxRASIS.setEnabled(False)
        self._ui.comboBoxLPSIS.setEnabled(False)
        self._ui.comboBoxRPSIS.setEnabled(False)
        self._ui.comboBoxSacral.setEnabled(False)
        self._ui.comboBoxLHJC.setEnabled(False)
        self._ui.comboBoxRHJC.setEnabled(False)
        self._ui.regButton.setEnabled(False)
        self._ui.resetButton.setEnabled(False)
        self._ui.acceptButton.setEnabled(False)
        self._ui.abortButton.setEnabled(False)

    def _regUnlockUI(self):
        self._ui.comboBoxRegMode.setEnabled(True)
        self._ui.spinBoxNPCs.setEnabled(True)
        self._ui.comboBoxLASIS.setEnabled(True)
        self._ui.comboBoxRASIS.setEnabled(True)
        self._ui.comboBoxLPSIS.setEnabled(True)
        self._ui.comboBoxRPSIS.setEnabled(True)
        self._ui.comboBoxSacral.setEnabled(True)
        self._ui.comboBoxLHJC.setEnabled(True)
        self._ui.comboBoxRHJC.setEnabled(True)
        self._ui.regButton.setEnabled(True)
        self._ui.resetButton.setEnabled(True)
        self._ui.acceptButton.setEnabled(True)
        self._ui.abortButton.setEnabled(True)

    def _reset(self):
        # delete viewer table row
        # self._ui.tableWidget.removeRow(2)
        # reset mesh
        meshObj = self._objects.getObject('pelvis mesh')
        meshObj.updateGeometry(self._origModel.get_field_parameters(), self._scene)
        # meshTableItem = self._ui.tableWidget.item(len(self._landmarkNames)-1,
        #                                           self.objectTableHeaderColumns['Visible'])
        # meshTableItem.setCheckState(Qt.Unchecked)

    def _accept(self):
        self._close()

    def _abort(self):
        self._reset()
        self._close()

    def _close(self):
        for name in self._objects.getObjectNames():
            self._objects.getObject(name).remove()

        self._objects._objects = {}
        self._objects == None

        # for r in xrange(self._ui.tableWidget.rowCount()):
        #     self._ui.tableWidget.removeRow(r)

    def _refresh(self):
        for r in range(self._ui.tableWidget.rowCount()):
            tableItem = self._ui.tableWidget.item(r, self.objectTableHeaderColumns['Visible'])
            name = tableItem.text()
            visible = tableItem.checkState().name == 'Checked'
            obj = self._objects.getObject(name)
            print(obj.name)
            if obj.sceneObject:
                print('changing existing visibility')
                obj.setVisibility(visible)
            else:
                print('drawing new')
                obj.draw(self._scene)

    def _saveScreenShot(self):
        filename = self._ui.screenshotFilenameLineEdit.text()
        width = int(self._ui.screenshotPixelXLineEdit.text())
        height = int(self._ui.screenshotPixelYLineEdit.text())
        self._scene.mlab.savefig(filename, size=(width, height))

    # ================================================================#
    @on_trait_change('scene.activated')
    def testPlot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        print('trait_changed')

        # We can do normal mlab calls on the embedded scene.
        self._scene.mlab.test_points3d()

    # def _saveImage_fired( self ):
    #     self.scene.mlab.savefig( str(self.saveImageFilename), size=( int(self.saveImageWidth), int(self.saveImageLength) ) )
