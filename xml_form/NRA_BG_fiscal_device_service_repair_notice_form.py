# encoding: windows-1251
import json
import glob
import pandas
SETTINGS = "config.json"


def xml_body(column_data) -> str:
    body = []
    for value in column_data:
        body.append(f"""
    <rowenum>
      <fdrid>{value}</fdrid>
   </rowenum>""")
    return "".join(body)


def main():
    with open(SETTINGS, encoding="utf-8") as config_data:
        config = json.load(config_data)

    if not glob.glob(f'{config["file"]}.xls*'):
        raise SystemExit(f'{config["file"]}.xls(x) is missing')
    else:
        table = "".join(glob.glob(f'{config["file"]}.xls*')[0])

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


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        raise SystemExit(f"{SETTINGS} is missing")
    except ValueError as e:
        raise SystemExit(e)
    except KeyError as e:
        raise SystemExit(f"Field {e} is missing")
    finally:
        input("Press <Enter> to close")
