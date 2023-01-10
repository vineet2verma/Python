
# it' will close All Excel Application 
# Without Saving it... 
import xlwings as xw

print("Start")
excel_app = xw.apps.active
excel_app.quit()
print("Complete")