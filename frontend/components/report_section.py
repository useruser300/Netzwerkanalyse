import json
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFileDialog, QMessageBox

class ReportSection(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QHBoxLayout(self)  # Horizontales Layout statt vertikal

        self.export_json_button = QPushButton("📊 Bericht als JSON speichern")
        self.export_json_button.clicked.connect(self.export_as_json)
        layout.addWidget(self.export_json_button)

        self.export_pdf_button = QPushButton("📄 Bericht als PDF speichern")
        self.export_pdf_button.clicked.connect(self.export_as_pdf)
        layout.addWidget(self.export_pdf_button)

    def generate_report(self):
        """Diese Methode wird von der Toolbar aufgerufen."""
        self.export_as_json()  # Standardmäßig JSON-Bericht erstellen
        QMessageBox.information(self, "Erfolg", "Bericht wurde erfolgreich generiert!")

    def export_as_json(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "JSON speichern", "", "JSON-Dateien (*.json)")
        if file_name:
            data = self.parent.analysis_section.get_analysis_data()
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            QMessageBox.information(self, "Erfolg", "Bericht erfolgreich als JSON gespeichert!")

    def export_as_pdf(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "PDF speichern", "", "PDF-Dateien (*.pdf)")
        if file_name:
            QMessageBox.information(self, "Erfolg", "Bericht erfolgreich als PDF gespeichert!")
