import sqlite3
from classes import Trap, User
import pandas as pd
import matplotlib.pyplot as plt
from werkzeug.security import generate_password_hash, check_password_hash


from recaptura_code import Ui_DataWindow
from calculos_code import Ui_GraphsWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel


import sys
from datetime import date, datetime

date_format = "%Y-%m-%d"
time_format = "%H:%M"

MAX_TRAP_NUMBER = 40

###############################
provinces_list = [
    "Galapagos",
    "Esmeraldas",
    "Manabi",
    "Los Rios",
    "Santa Elena",
    "Guayas",
    "Santo Domingo de los Tsachilas",
    "El Oro",
]
galapagos_county_list = ["Santa Cruz", "Isabela", "San Cristobal"]
location_list = ["Bellavista"]
species_list = ["AEG", "CUX", "Taenorhincus"]
trap_methods_list = ["BG-SENTINEL"]
##############################


############################
# df_csv = pd.read_csv('MRR_ECU.csv', encoding="ISO-8859-1")
# print(df_csv)
# # print(df_csv)
##########################

# def get_trap_by_code(code):
#     c.execute("SELECT * FROM recapture WHERE trap_code=:trap_code", {"trap_code": code})
#     trap_info = c.fetchone()
#     (
#         country,
#         province,
#         county,
#         location,
#         long,
#         latt,
#         altitude,
#         trap_code,
#         trap_methods,
#         trap_installation_date,
#         release_date,
#         release_time,
#         collection_date,
#         collection_time,
#         temperature,
#         humidity,
#         AEG_pink_male,
#         AEG_pink_female,
#         AEG_yellow_male,
#         AEG_yellow_female,
#         AEG_nomarked_male,
#         AEG_nomarked_female,
#         CUX_nomarked_male,
#         CUX_nomarked_female,
#         taenorhincus_nomarked_male,
#         taenorhincus_nomarked_female,
#         OBS,
#     ) = trap_info
#     trap = Trap(
#         country,
#         province,
#         county,
#         location,
#         long,
#         latt,
#         altitude,
#         trap_code,
#         trap_methods,
#         trap_installation_date,
#         release_date,
#         release_time,
#         collection_date,
#         collection_time,
#         temperature,
#         humidity,
#         AEG_pink_male,
#         AEG_pink_female,
#         AEG_yellow_male,
#         AEG_yellow_female,
#         AEG_nomarked_male,
#         AEG_nomarked_female,
#         CUX_nomarked_male,
#         CUX_nomarked_female,
#         taenorhincus_nomarked_male,
#         taenorhincus_nomarked_female,
#         OBS,
#     )
#     return trap

# trap = get_trap_by_code("BG-1")
# print(trap.trap_code)


class WindowUi(qtw.QMainWindow, Ui_DataWindow):
    def __init__(self, *args, **kwargs):
        super(WindowUi, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # self.setWindowIcon(qtg.QIcon("logo256png.png"))
        # screen = qta.screens()[0]
        # dpiScaling = screen.logicalDotsPerInch()
        # self.scalingLabel = QLabel("DPI scaling: " + str(dpiScaling))

        for each in provinces_list:
            self.comboBox_province.addItem(each)
        for each in galapagos_county_list:
            self.comboBox_county.addItem(each)
        for each in location_list:
            self.comboBox_location.addItem(each)

        for each in species_list:
            self.comboBox_species.addItem(each)

        for each in trap_methods_list:
            self.comboBox_method.addItem(each)
        for i in range(1, MAX_TRAP_NUMBER + 1):
            self.comboBox_code.addItem(f"BG-{i}")

        self.pushButton.clicked.connect(self.input_data)
        self.pushButton_save_quantity.clicked.connect(self.save_quantity)

        self.AEG_pink_male = 0
        self.AEG_pink_female = 0
        self.AEG_yellow_male = 0
        self.AEG_yellow_female = 0
        self.AEG_nomarked_male = 0
        self.AEG_nomarked_female = 0
        self.CUX_nomarked_male = 0
        self.CUX_nomarked_female = 0
        self.taenorhincus_nomarked_male = 0
        self.taenorhincus_nomarked_female = 0

    def save_quantity(self):
        self.species = self.comboBox_species.currentText()
        self.color = self.comboBox_color.currentText()
        self.sex = self.comboBox_sex.currentText()

        try:
            if int(self.lineEdit_quantity.text()) < 0:
                qtw.QMessageBox.information(
                    self, "Error", "Ingrese parametros numéricos enteros positivos"
                )
                return
            if self.lineEdit_quantity.text() == "":
                self.quantity = None
                return
            self.quantity = self.lineEdit_quantity.text()

            if self.species == "AEG" and self.color == "rosado" and self.sex == "macho":
                self.AEG_pink_male = int(self.quantity)
            if (
                self.species == "AEG"
                and self.color == "rosado"
                and self.sex == "hembra"
            ):
                self.AEG_pink_female = int(self.quantity)
            if (
                self.species == "AEG"
                and self.color == "amarillo"
                and self.sex == "macho"
            ):
                self.AEG_yellow_male = int(self.quantity)
            if (
                self.species == "AEG"
                and self.color == "amarillo"
                and self.sex == "hembra"
            ):
                self.AEG_yellow_female = int(self.quantity)
            if (
                self.species == "AEG"
                and self.color == "no color"
                and self.sex == "macho"
            ):
                self.AEG_nomarked_male = int(self.quantity)
            if (
                self.species == "AEG"
                and self.color == "no color"
                and self.sex == "hembra"
            ):
                self.AEG_nomarked_female = int(self.quantity)
            if (
                self.species == "CUX"
                and self.color == "no color"
                and self.sex == "macho"
            ):
                self.CUX_nomarked_male = int(self.quantity)
            if (
                self.species == "CUX"
                and self.color == "no color"
                and self.sex == "hembra"
            ):
                self.CUX_nomarked_female = int(self.quantity)
            if (
                self.species == "Taenorhincus"
                and self.color == "no color"
                and self.sex == "macho"
            ):
                self.taenorhincus_nomarked_male = int(self.quantity)
            if (
                self.species == "Taenorhincus"
                and self.color == "no color"
                and self.sex == "hembra"
            ):
                self.taenorhincus_nomarked_female = int(self.quantity)
            # print(self.AEG_yellow_male)
            self.textEdit_summary.setPlainText(
                f"AEG rosados macho: {self.AEG_pink_male}\nAEG rosados hembra: {self.AEG_pink_female}\nAEG amarillos macho: {self.AEG_yellow_male}\nAEG amarillos hembra: {self.AEG_yellow_female}\nAEG sin color macho: {self.AEG_nomarked_male}\nAEG sin color hembra: {self.AEG_nomarked_female}\nCUX sin color macho: {self.CUX_nomarked_male}\nCUX sin color hembra: {self.CUX_nomarked_female}\nTaenorhincus sin color macho: {self.taenorhincus_nomarked_male}\nTaenorhincus sin color hembra: {self.taenorhincus_nomarked_female}\n"
            )

        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese parametros numéricos enteros positivo"
            )
            return

    def input_data(self):
        self.country = self.lineEdit_country.text()
        self.province = self.comboBox_province.currentText()
        self.county = self.comboBox_county.currentText()
        self.location = self.comboBox_location.currentText()

        try:
            if self.lineEdit_latt.text() == "":
                self.latt = None
            else:
                if (
                    float(self.lineEdit_latt.text()) < -90
                    or float(self.lineEdit_latt.text()) > 90
                ):
                    qtw.QMessageBox.information(
                        self, "Error", "Ingrese latitud en decimales entre -90 y 90"
                    )
                    return
                self.latt = float(self.lineEdit_latt.text())
        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese latitud en decimales entre -90 y 90"
            )
            return
        try:
            if self.lineEdit_long.text() == "":
                self.long = None
            else:
                if (
                    float(self.lineEdit_long.text()) < -180
                    or float(self.lineEdit_long.text()) > 180
                ):
                    qtw.QMessageBox.information(
                        self, "Error", "Ingrese longitud en decimales entre -180 y 180"
                    )
                    return
                self.long = float(self.lineEdit_long.text())
        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese latitud en decimales entre -180 y 180"
            )
            return
        try:
            if self.lineEdit_altitude.text() == "":
                self.altitude = None
            else:
                if (
                    float(self.lineEdit_altitude.text()) < 0
                    or float(self.lineEdit_altitude.text()) > 4000
                ):
                    qtw.QMessageBox.information(
                        self, "Error", "Ingrese altitud en decimales entre 0 y 4000"
                    )
                    return
                self.altitude = float(self.lineEdit_altitude.text())
        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese altitud en decimales entre 0 y 4000"
            )
            return

        self.trap_code = self.comboBox_code.currentText()
        self.method = self.comboBox_method.currentText()

        try:
            is_date = bool(
                datetime.strptime(self.lineEdit_installation.text(), date_format)
            )
            is_date = bool(datetime.strptime(self.lineEdit_release.text(), date_format))

            self.installation_date = self.lineEdit_installation.text()
            self.release_date = self.lineEdit_release.text()

        except ValueError:
            is_date = False
            qtw.QMessageBox.information(self, "Error", "Ingrese una fecha: aaaa-mm-dd")
            return

        try:
            if self.lineEdit_collection.text() == "":
                self.collection_date = None
                self.AEG_pink_male = None
                self.AEG_pink_female = None
                self.AEG_yellow_male = None
                self.AEG_yellow_female = None
                self.AEG_nomarked_male = None
                self.AEG_nomarked_female = None
                self.CUX_nomarked_male = None
                self.CUX_nomarked_female = None
                self.taenorhincus_nomarked_male = None
                self.taenorhincus_nomarked_female = None
            else:
                is_date = bool(
                    datetime.strptime(self.lineEdit_collection.text(), date_format)
                )
                self.collection_date = self.lineEdit_collection.text()
        except ValueError:
            is_date = False
            qtw.QMessageBox.information(self, "Error", "Ingrese una fecha: aaaa-mm-dd")
            return

        try:
            if self.lineEdit_collection_time.text() == "":
                self.collection_time = None
            else:
                is_time = bool(
                    datetime.strptime(self.lineEdit_collection_time.text(), time_format)
                )
                self.collection_time = self.lineEdit_collection_time.text()
        except ValueError:
            is_time = False
            qtw.QMessageBox.information(
                self, "Error", "Ingrese una hora: HH:MM [24 horas]"
            )
            return

        try:
            is_time = bool(
                datetime.strptime(self.lineEdit_release_time.text(), time_format)
            )

            self.release_time = self.lineEdit_release_time.text()

        except ValueError:
            is_time = False
            qtw.QMessageBox.information(
                self, "Error", "Ingrese una hora: HH:MM [24 horas]"
            )
            return

        try:
            if self.lineEdit_temp.text() == "":
                self.temperature = None
            else:
                if (
                    float(self.lineEdit_temp.text()) < 0
                    or float(self.lineEdit_temp.text()) > 50
                ):
                    qtw.QMessageBox.information(
                        self, "Error", "Ingrese temperatura en decimales entre 0 y 50"
                    )
                    return
                self.temperature = float(self.lineEdit_temp.text())
        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese temperatura en decimales entre 0 y 50"
            )
            return
        try:
            if self.lineEdit_humi.text() == "":
                self.humidity = None
            else:
                if (
                    float(self.lineEdit_humi.text()) < 0
                    or float(self.lineEdit_humi.text()) > 100
                ):
                    qtw.QMessageBox.information(
                        self, "Error", "Ingrese humedad en decimales entre 0 y 100"
                    )
                    return
                self.humidity = float(self.lineEdit_humi.text())
        except ValueError:
            qtw.QMessageBox.information(
                self, "Error", "Ingrese humedad en decimales entre 0 y 100"
            )
            return

        self.observations = str(self.textEdit.toPlainText())

        fields_list = [
            self.country,
            self.province,
            self.county,
            self.location,
            self.latt,
            self.long,
            self.altitude,
            self.trap_code,
            self.method,
            self.installation_date,
            self.release_date,
            self.release_time,
            self.collection_date,
            self.collection_time,
            self.temperature,
            self.humidity,
            self.AEG_pink_male,
            self.AEG_pink_female,
            self.AEG_yellow_male,
            self.AEG_yellow_female,
            self.AEG_nomarked_male,
            self.AEG_nomarked_female,
            self.CUX_nomarked_male,
            self.CUX_nomarked_female,
            self.taenorhincus_nomarked_male,
            self.taenorhincus_nomarked_female,
            self.observations,
        ]
        for each in fields_list:
            if each == "":
                each = None

        conn = sqlite3.connect("recapture.db")

        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM recapture", conn)

        c.execute(
            """UPDATE recapture SET country = :country, province = :province, 
                county = :county, location = :location, latt = :latt, 
                long = :long, altitude  = :altitude, trap_methods = :method, 
                trap_installation_date  = :installation_date, release_date  = :release_date, 
                release_time = :release_time, collection_date = :collection_date, 
                collection_time = :collection_time, temperature = :temperature, 
                humidity = :humidity, AEG_pink_male = :AEG_pink_male, 
                AEG_pink_female = :AEG_pink_female, AEG_yellow_male = :AEG_yellow_male, 
                AEG_yellow_female = :AEG_yellow_female, AEG_nomarked_male = :AEG_nomarked_male, 
                AEG_nomarked_female = :AEG_nomarked_female, CUX_nomarked_male = :CUX_nomarked_male, 
                CUX_nomarked_female = :CUX_nomarked_female, taenorhincus_nomarked_male = :taenorhincus_nomarked_male, 
                taenorhincus_nomarked_female = :taenorhincus_nomarked_female, OBS = :observations WHERE trap_code = :trap_code""",
            {
                "country": self.country,
                "province": self.province,
                "county": self.county,
                "location": self.location,
                "latt": self.latt,
                "long": self.long,
                "altitude": self.altitude,
                "trap_code": self.trap_code,
                "method": self.method,
                "installation_date": self.installation_date,
                "release_date": self.release_date,
                "release_time": self.release_time,
                "collection_date": self.collection_date,
                "collection_time": self.collection_time,
                "temperature": self.temperature,
                "humidity": self.humidity,
                "AEG_pink_male": self.AEG_pink_male,
                "AEG_pink_female": self.AEG_pink_female,
                "AEG_yellow_male": self.AEG_yellow_male,
                "AEG_yellow_female": self.AEG_yellow_female,
                "AEG_nomarked_male": self.AEG_nomarked_male,
                "AEG_nomarked_female": self.AEG_nomarked_female,
                "CUX_nomarked_male": self.CUX_nomarked_male,
                "CUX_nomarked_female": self.CUX_nomarked_female,
                "taenorhincus_nomarked_male": self.taenorhincus_nomarked_male,
                "taenorhincus_nomarked_female": self.taenorhincus_nomarked_female,
                "observations": self.observations,
            },
        )

        conn.commit()
        if c.rowcount < 1:
            print(c.rowcount)
            qtw.QMessageBox.information(
                self, "Error", f"Error en modificar fila {self.trap_code}"
            )
        else:
            qtw.QMessageBox.information(
                self, "Exito", f"Fila {self.trap_code} modificada"
            )
        conn.close()


class GraphsWindow(qtw.QMainWindow, Ui_GraphsWindow):
    def __init__(self, *args, **kwargs):
        super(GraphsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_get_graphs.clicked.connect(self.calculate_graphs)

    def calculate_graphs(self):
        conn = sqlite3.connect("recapture.db")

        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM recapture", conn)
        conn.close()

        df = pd.melt(
            df,
            id_vars=[
                "country",
                "province",
                "county",
                "location",
                "long",
                "latt",
                "altitude",
                "trap_code",
                "trap_methods",
                "trap_installation_date",
                "release_date",
                "release_time",
                "collection_date",
                "collection_time",
                "temperature",
                "humidity",
                "OBS",
            ],
            value_vars=[
                "AEG_pink_male",
                "AEG_pink_male",
                "AEG_pink_female",
                "AEG_yellow_male",
                "AEG_yellow_female",
                "AEG_nomarked_male",
                "AEG_nomarked_female",
                "CUX_nomarked_male",
                "CUX_nomarked_female",
                "taenorhincus_nomarked_male",
                "taenorhincus_nomarked_female",
            ],
            var_name="species",
            value_name="total_collected",
        )

        def color_case(color):
            if (color == "pink").any():
                return 14000
            elif (color == "yellow").any():
                return 44000
            else:
                return None

        def recapture_rate(marked_released, total_collected):
            return total_collected / marked_released * 100

        df[["species", "color", "sex"]] = df.species.str.split("_", expand=True)
        df["release_date"] = pd.to_datetime(df.release_date)
        df["collection_date"] = pd.to_datetime(df.collection_date)
        df["trap_installation_date"] = pd.to_datetime(df.trap_installation_date)
        print(df.to_string())
        df["marked_released"] = df.groupby("color")["color"].transform(color_case)

        df["recapture_rate"] = df.groupby("trap_code")["marked_released"].transform(
            recapture_rate, df["total_collected"]
        )

        df_marked = df.loc[df["color"] != "nomarked"]
        df_nofemale = df_marked.loc[df["sex"] != "female"]

        df_pink = df_nofemale.loc[df_nofemale["color"] == "pink"]
        df_yellow = df_nofemale.loc[df_nofemale["color"] == "yellow"]
        recap_rate_pink = df_pink["total_collected"].sum() / 14000 * 100
        recap_rate_yellow = df_yellow["total_collected"].sum() / 44000 * 100
        print(recap_rate_pink)
        print(recap_rate_yellow)

        df_nomarked = df.loc[df["color"] == "nomarked"]
        df_nomarked_AEG = df_nomarked.loc[df["species"] == "AEG"]
        df_males = df.loc[df["sex"] == "male"]
        df_females = df.loc[df["sex"] == "female"]

        df_sex_total_collected = df_nomarked_AEG.pivot(
            index=["trap_code"], columns="sex", values=["total_collected"]
        )

        d = {
            "female": df_sex_total_collected["total_collected"]["female"],
            "male": df_sex_total_collected["total_collected"]["male"],
        }
        new_df_box = pd.DataFrame(data=d)

        b_plot = new_df_box.boxplot(column=["female", "male"])
        b_plot.plot()
        axes1 = df_nofemale.loc[df["color"] == "pink"].plot.bar(
            x="trap_code",
            y="recapture_rate",
        )
        axes2 = df_nofemale.loc[df["color"] == "yellow"].plot.bar(
            x="trap_code",
            y="recapture_rate",
        )
        plt.show()


if __name__ == "__main__":
    import sys

    app = qtw.QApplication(sys.argv)
    windowUi = WindowUi()
    graphsWindow = GraphsWindow()
    windowUi.show()
    graphsWindow.show()

    sys.exit(app.exec_())
