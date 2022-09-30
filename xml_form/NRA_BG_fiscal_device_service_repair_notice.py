# encoding: windows-1251
import json
import glob
import pandas


def xml_body(column_data) -> str:
    body = []
    for value in column_data:
        body.append(f"""
    <rowenum>
      <fdrid>{value}</fdrid>
   </rowenum>""")
    return "".join(body)


try:
    with open("config.json", encoding="utf-8") as config_data:
        config = json.load(config_data)

    table = "".join(glob.glob("1.xls*")[0])

    # pandas.read_excel("1.xls", sheet_name="Задания за сервиз2", header=1, usecols=("J"))
    df = pandas.read_excel(table, sheet_name="Задания за сервиз2", header=1)
    reg_numbers = df["Регистрационен номер в НАП"].tolist()
    company_id = df["Идентификационен No."].values[2]
    company_name = df["Име"].values[2]

    xml_header = f"""<?xml version="1.0" encoding="WINDOWS-1251"?>
<dec44a2 xmlns="http://inetdec.nra.bg/xsd/dec_44a2.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://inetdec.nra.bg/xsd/dec_44a2.xsd http://inetdec.nra.bg/xsd/dec_44a2.xsd">
  <name>{config["name"]}</name>
  <bulstat>{config["bulstat"]}</bulstat>
  <telcode>{config["telcode"]}</telcode>
  <telnum>{config["telnum"]}</telnum>
  <authorizeid>{config["authorizeid"]}</authorizeid>
  <autorizecode>{config["autorizecode"]}</autorizecode>
  <fname>{config["fname"]}</fname>
  <sname>{config["sname"]}</sname>
  <tname>{config["tname"]}</tname>
  <id>{company_id}</id>
  <code>{config["code"]}</code>
  <fuiasutd>"""

    xml_footer = """
  </fuiasutd>
</dec44a2>"""

    with open(f"{company_id} {company_name}.xml", "w", encoding="windows-1251") as file:
        file.write(xml_header + xml_body(reg_numbers) + xml_footer)

except FileNotFoundError as e:
    print(e)
except IndexError as e:
    print("1.xls or 1.xlsx file is not found")
except ValueError as e:
    print(e)
except KeyError as e:
    print(f"Field {e} is not found")
