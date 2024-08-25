import dz12 as dzlogger
x = '3285*210-123+854/12'
dzlogger.writeFile(f"{x}")
dzlogger.writeFile(f"= {eval(x)}")
