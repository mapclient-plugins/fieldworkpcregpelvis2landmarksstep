from PySide6 import QtWidgets
from mapclientplugins.fieldworkpcregpelvis2landmarksstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''

REGMODES = {'PC': 1,
            'Linear Scaling': 2,
            }


class ConfigureDialog(QtWidgets.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._setupDialog()
        self._makeConnections()

    def _setupDialog(self):
        self._ui.comboBoxRegMode.addItem('PC')
        self._ui.comboBoxRegMode.addItem('Linear Scaling')
        self._ui.spinBoxNPCs.setSingleStep(1)

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        config['regMode'] = REGMODES[self._ui.comboBoxRegMode.currentText()]
        config['npcs'] = self._ui.spinBoxNPCs.value()
        config['LASIS'] = self._ui.lineEditLASIS.text()
        config['RASIS'] = self._ui.lineEditRASIS.text()
        config['LPSIS'] = self._ui.lineEditLPSIS.text()
        config['RPSIS'] = self._ui.lineEditRPSIS.text()
        config['Sacral'] = self._ui.lineEditSacral.text()
        config['LHJC'] = self._ui.lineEditLHJC.text()
        config['RHJC'] = self._ui.lineEditRHJC.text()
        config['GUI'] = self._ui.checkBoxGUI.isChecked()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        self._ui.comboBoxRegMode.setCurrentIndex(config['regMode'] - 1)
        self._ui.spinBoxNPCs.setValue(config['npcs'])
        self._ui.lineEditLASIS.setText(config['LASIS'])
        self._ui.lineEditRASIS.setText(config['RASIS'])
        self._ui.lineEditLPSIS.setText(config['LPSIS'])
        self._ui.lineEditRPSIS.setText(config['RPSIS'])
        self._ui.lineEditSacral.setText(config['Sacral'])
        self._ui.lineEditLHJC.setText(config['LHJC'])
        self._ui.lineEditRHJC.setText(config['RHJC'])
        self._ui.checkBoxGUI.setChecked(bool(config['GUI']))
